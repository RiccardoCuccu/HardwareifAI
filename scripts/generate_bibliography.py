#!/usr/bin/env python3
"""
Aggregates GFM footnotes ([^label] ... [^label]: text) scattered across the
HardwareifAI repository's Markdown files into five category bibliography
files under references/: papers.md, repositories.md, books.md, articles.md,
courses.md.

In the curriculum modules, footnotes are written as usual: they remain
clickable and with automatic return thanks to GitHub's native rendering.
This script reads them, classifies each cited source into one of four
categories, and (re)writes the corresponding auto-generated section of each
output file.

Each output file has three parts:
  1. A preamble (H1 title + one-line description) above "## Bibliography".
     Entirely hand-owned: the script never writes to it except to create a
     bare placeholder the first time a category file is generated.
  2. The "## Bibliography" section itself, fully owned by the script and
     rewritten in full on every run (heading, disclaimer, entries).
  3. A hand-curated "## Extra" section, preserved verbatim across runs.

Usage:
    python generate_bibliography.py
    python generate_bibliography.py --dry-run
    python generate_bibliography.py --repo-root C:\\path\\to\\HardwareifAI

Required convention: the same source must ALWAYS use the same label
(e.g., always "turing1950") in all files where it is cited.
"""

import argparse
import io
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

FOOTNOTE_DEF_RE = re.compile(r"^\[\^([\w-]+)\]:\s?(.*)$")
FOOTNOTE_REF_RE = re.compile(r"\[\^([\w-]+)\](?!:)")
URL_RE = re.compile(r"https?://\S+")

# Directory names excluded anywhere in the path when walking the repo for
# Markdown files (checked against each path component, not just the root).
EXCLUDED_DIR_NAMES = frozenset({".git", "scripts"})

# URL substrings (checked case-insensitively) that identify a scientific
# paper. Checked first: this category takes priority over repository/book/
# course.
PAPER_URL_MARKERS = ("doi.org", "arxiv.org")

# URL substrings (checked case-insensitively) that identify a code
# repository. Checked second, right after paper: both are reliable
# domain-based checks, so repository is resolved before book/course/article
# text-based heuristics can misclassify it.
REPOSITORY_URL_MARKERS = ("github.com", "huggingface.co")

# Publisher-name keywords (checked case-sensitively against the raw
# definition text) that identify a book citation.
BOOK_KEYWORDS = (
    "Press",
    "Publishing",
    "Morgan Kaufmann",
    "O'Reilly",
    "Addison-Wesley",
    "Holloway",
)

# Course-platform domains (matched against the URL's netloc) that identify a
# course citation.
COURSE_DOMAINS = (
    "coursera.org",
    "edx.org",
    "ocw.mit.edu",
)

CATEGORY_PAPER = "paper"
CATEGORY_REPOSITORY = "repository"
CATEGORY_BOOK = "book"
CATEGORY_COURSE = "course"
CATEGORY_ARTICLE = "article"
CATEGORIES = (
    CATEGORY_PAPER,
    CATEGORY_REPOSITORY,
    CATEGORY_BOOK,
    CATEGORY_ARTICLE,
    CATEGORY_COURSE,
)

CATEGORY_FILENAMES = {
    CATEGORY_PAPER: "papers.md",
    CATEGORY_REPOSITORY: "repositories.md",
    CATEGORY_BOOK: "books.md",
    CATEGORY_ARTICLE: "articles.md",
    CATEGORY_COURSE: "courses.md",
}

CATEGORY_TITLES = {
    CATEGORY_PAPER: "Papers",
    CATEGORY_REPOSITORY: "Repositories",
    CATEGORY_BOOK: "Books",
    CATEGORY_ARTICLE: "Articles",
    CATEGORY_COURSE: "Courses",
}

BIBLIOGRAPHY_HEADING = "## Bibliography"
BIBLIOGRAPHY_SECTION_RE = re.compile(r"^## Bibliography\s*$", re.MULTILINE)

EXTRA_HEADING = "## Extra"
EXTRA_SECTION_RE = re.compile(r"^## Extra\s*$", re.MULTILINE)
EXTRA_PLACEHOLDER = "<!-- Add hand-curated entries below this line. -->"
EXTRA_LABEL_RE = re.compile(r"^\*\*\[([\w-]+)\]\*\*")

GENERATED_NOTICE = (
    "_Generated automatically by `generate_bibliography.py`: "
    "do not edit manually above the `## Extra` section._"
)


def extract_footnotes(md_path: Path) -> tuple[dict[str, str], set[str]]:
    """Extracts footnote definitions and citations from a single Markdown file.

    Args:
        md_path: Path to the Markdown file to parse.

    Returns:
        A tuple of (definitions, citations): definitions maps each footnote
        label to its definition text, citations is the set of labels
        referenced via `[^label]` anywhere in the file (including in
        definitions of other labels).

    Raises:
        FileNotFoundError: If md_path does not exist.
        IOError: If md_path cannot be read for any other reason.
    """
    definitions: dict[str, str] = {}
    citations: set[str] = set()

    try:
        lines = md_path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Module file not found: {md_path}")
    except OSError as exc:
        raise IOError(f"Failed to read {md_path}: {exc}")

    i = 0
    while i < len(lines):
        line = lines[i]
        match = FOOTNOTE_DEF_RE.match(line)
        if match:
            label, text = match.group(1), match.group(2)
            # Capture any indented continuation lines (multi-line definitions)
            i += 1
            while (
                i < len(lines)
                and lines[i].strip() != ""
                and lines[i].startswith((" ", "\t"))
            ):
                text += " " + lines[i].strip()
                i += 1
            definitions[label] = text.strip()
            continue

        for ref in FOOTNOTE_REF_RE.findall(line):
            citations.add(ref)
        i += 1

    return definitions, citations


def classify_footnote(text: str) -> str:
    """Classifies a footnote definition into one of the five categories.

    Checks in priority order (first match wins): paper (doi.org/arxiv.org
    URL), repository (github.com/huggingface.co URL), book (publisher-name
    keyword), course (course-platform domain), falling back to article for
    everything else.

    Args:
        text: The raw footnote definition text (citation prose plus URL).

    Returns:
        One of CATEGORY_PAPER, CATEGORY_REPOSITORY, CATEGORY_BOOK,
        CATEGORY_COURSE, CATEGORY_ARTICLE.
    """
    urls = URL_RE.findall(text)

    if any(marker in url.lower() for url in urls for marker in PAPER_URL_MARKERS):
        return CATEGORY_PAPER

    if any(
        marker in url.lower() for url in urls for marker in REPOSITORY_URL_MARKERS
    ):
        return CATEGORY_REPOSITORY

    if any(keyword in text for keyword in BOOK_KEYWORDS):
        return CATEGORY_BOOK

    for url in urls:
        domain = urlparse(url).netloc.lower()
        if any(domain == d or domain.endswith(f".{d}") for d in COURSE_DOMAINS):
            return CATEGORY_COURSE

    return CATEGORY_ARTICLE


def discover_markdown_files(
    repo_root: Path, excluded_output_paths: set[Path]
) -> list[Path]:
    """Recursively finds Markdown files under the repo root.

    Args:
        repo_root: Root directory to scan.
        excluded_output_paths: Resolved paths of the output files this
            script writes; these are never treated as sources.

    Returns:
        Sorted list of Markdown file paths, excluding EXCLUDED_DIR_NAMES
        directories and the output files themselves.

    Raises:
        FileNotFoundError: If repo_root does not exist.
    """
    if not repo_root.exists():
        raise FileNotFoundError(f"Repository root not found: {repo_root}")

    md_files = []
    for path in repo_root.rglob("*.md"):
        rel_parts = path.relative_to(repo_root).parts[:-1]
        if any(part in EXCLUDED_DIR_NAMES for part in rel_parts):
            continue
        if path.resolve() in excluded_output_paths:
            continue
        md_files.append(path)

    return sorted(md_files)


def collect_bibliography(
    md_files: list[Path], repo_root: Path
) -> tuple[dict[str, str], dict[str, str], dict[str, set[str]], list[tuple[str, str]]]:
    """Aggregates footnote definitions and backlinks across all Markdown files.

    Args:
        md_files: Markdown files to scan, in any order.
        repo_root: Root directory used to compute repo-relative backlink paths.

    Returns:
        A tuple of (definitions, label_category, cited_in, conflicts):
        definitions maps label to its (first-seen) definition text,
        label_category maps label to its classified category, cited_in maps
        label to the set of repo-relative file paths that cite or define it,
        and conflicts lists (label, file) pairs where a later file defined
        the same label with different text.
    """
    definitions: dict[str, str] = {}
    label_category: dict[str, str] = {}
    cited_in: dict[str, set[str]] = defaultdict(set)
    conflicts: list[tuple[str, str]] = []

    for md_path in md_files:
        file_definitions, citations = extract_footnotes(md_path)
        rel = md_path.relative_to(repo_root).as_posix()

        for label, text in file_definitions.items():
            if label in definitions and definitions[label] != text:
                conflicts.append((label, rel))
            else:
                definitions.setdefault(label, text)
                label_category.setdefault(label, classify_footnote(text))

        for label in citations | file_definitions.keys():
            cited_in[label].add(rel)

    return definitions, label_category, cited_in, conflicts


def extract_preamble(output_path: Path) -> str | None:
    """Reads the hand-owned preamble (H1 + description) above "## Bibliography".

    The preamble is never written or modified by this script beyond initial
    placeholder creation: it is read back verbatim on every run and
    reproduced unchanged in the regenerated file.

    Args:
        output_path: Path to a previously generated output file, if any.

    Returns:
        The verbatim text from the start of the file up to (but excluding)
        the "## Bibliography" heading, with trailing newlines stripped, or
        None if the file does not exist or has no "## Bibliography" heading
        yet (first run for this category, or pre-migration file).
    """
    if not output_path.exists():
        return None

    content = output_path.read_text(encoding="utf-8")
    match = BIBLIOGRAPHY_SECTION_RE.search(content)
    if not match:
        return None

    return content[: match.start()].rstrip("\n")


def extract_extra_section(output_path: Path) -> str:
    """Reads the existing "## Extra" section (heading included) from a file.

    Args:
        output_path: Path to a previously generated output file, if any.

    Returns:
        The verbatim text from "## Extra" to end of file, with trailing
        newlines stripped, or an empty string if the file does not exist or
        has no "## Extra" section.
    """
    if not output_path.exists():
        return ""

    content = output_path.read_text(encoding="utf-8")
    match = EXTRA_SECTION_RE.search(content)
    if not match:
        return ""

    return content[match.start():].rstrip("\n")


def extract_auto_urls(entries: dict[str, str]) -> dict[str, str]:
    """Maps each URL found in auto-generated entries to its citation label.

    Args:
        entries: Mapping of label to definition text for one category's
            auto-generated entries.

    Returns:
        Mapping of URL to the label of the entry it was found in.
    """
    url_to_label: dict[str, str] = {}
    for label, text in entries.items():
        for url in URL_RE.findall(text):
            url_to_label[url] = label
    return url_to_label


def extract_extra_urls(existing_extra: str) -> dict[str, str]:
    """Maps each URL found in the "## Extra" section to its entry identifier.

    Args:
        existing_extra: Verbatim "## Extra" section text (heading included),
            as returned by extract_extra_section.

    Returns:
        Mapping of URL to a short human-readable identifier for the entry it
        was found in: the bracketed label (e.g. "[devlin2018]") if the entry
        follows the bolded-label convention, otherwise the entry's first
        line.
    """
    url_to_entry: dict[str, str] = {}
    blocks = re.split(r"\n\s*\n", existing_extra)

    for block in blocks:
        block = block.strip()
        if not block or block == EXTRA_HEADING or block == EXTRA_PLACEHOLDER:
            continue

        label_match = EXTRA_LABEL_RE.match(block)
        identifier = (
            f"[{label_match.group(1)}]" if label_match else block.splitlines()[0].strip()
        )
        for url in URL_RE.findall(block):
            url_to_entry[url] = identifier

    return url_to_entry


def warn_duplicate_urls(
    output_filename: str, entries: dict[str, str], existing_extra: str
) -> None:
    """Warns when a URL appears in both the auto-generated and Extra sections.

    This is a report-only check: it never modifies the Extra section. It
    flags resources that have since become real citations (footnotes) so a
    human can remove the now-redundant hand-curated entry.

    Args:
        output_filename: Name of the output file being checked (used only
            in the warning message).
        entries: Mapping of label to definition text for this category's
            auto-generated entries.
        existing_extra: Verbatim "## Extra" section text, as returned by
            extract_extra_section. May be empty if the file has no Extra
            section yet.
    """
    if not existing_extra:
        return

    auto_urls = extract_auto_urls(entries)
    extra_urls = extract_extra_urls(existing_extra)

    for url, extra_entry in extra_urls.items():
        auto_label = auto_urls.get(url)
        if auto_label is not None:
            log.warning(
                "%s: URL %s appears in both the auto-generated entry [%s] "
                "and the Extra entry %s (remove the stale Extra entry).",
                output_filename,
                url,
                auto_label,
                extra_entry,
            )


def render_category_file(
    category: str,
    entries: dict[str, str],
    cited_in: dict[str, set[str]],
    existing_extra: str,
    preamble: str | None,
) -> str:
    """Builds the full contents of one category's output file.

    Args:
        category: One of the CATEGORIES constants.
        entries: Mapping of label to definition text for this category only.
        cited_in: Global label-to-backlinks mapping (shared across categories).
        existing_extra: Verbatim "## Extra" section preserved from a prior
            run, or empty string if none exists yet.
        preamble: Verbatim hand-owned preamble (H1 + description) preserved
            from a prior run, as returned by extract_preamble. If None (no
            prior run for this category), a bare "# {Title}" placeholder is
            used so the file is well-formed; a human is expected to add a
            one-line description afterward.

    Returns:
        The complete Markdown text to write to the output file.
    """
    if preamble is None:
        preamble = f"# {CATEGORY_TITLES[category]}"
        log.warning(
            "%s: no existing preamble found above `## Bibliography`; "
            "writing a bare H1 placeholder (add a one-line description "
            "manually).",
            CATEGORY_FILENAMES[category],
        )

    lines = preamble.rstrip("\n").split("\n")
    lines += ["", BIBLIOGRAPHY_HEADING, "", GENERATED_NOTICE, ""]

    if entries:
        for label in sorted(entries):
            text = entries[label]
            backlinks = ", ".join(
                f"[{path}]({path})" for path in sorted(cited_in[label])
            )
            lines.append(f"**[{label}]** {text}  ")
            lines.append(f"Cited in: {backlinks}")
            lines.append("")
    else:
        lines.append("_No entries yet._")
        lines.append("")

    if existing_extra:
        lines.append(existing_extra)
    else:
        lines.append(EXTRA_HEADING)
        lines.append("")
        lines.append(EXTRA_PLACEHOLDER)

    lines.append("")
    return "\n".join(lines)


def main(args: argparse.Namespace) -> int:
    """Main entry point: scans the repo, classifies footnotes, writes output.

    Args:
        args: Parsed CLI arguments.

    Returns:
        Exit code (0 = success, 1 = failure).
    """
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

    repo_root = args.repo_root.resolve()
    output_dir = (args.output_dir or (repo_root / "references")).resolve()
    output_paths = {
        (output_dir / filename).resolve() for filename in CATEGORY_FILENAMES.values()
    }

    try:
        md_files = discover_markdown_files(repo_root, output_paths)
    except FileNotFoundError as exc:
        log.error(str(exc))
        return 1

    definitions, label_category, cited_in, conflicts = collect_bibliography(
        md_files, repo_root
    )

    for label, rel in conflicts:
        log.warning(
            "Label [%s] redefined with different text in %s (check manually).",
            label,
            rel,
        )

    entries_by_category: dict[str, dict[str, str]] = {
        category: {} for category in CATEGORIES
    }
    for label, text in definitions.items():
        entries_by_category[label_category[label]][label] = text

    for category in CATEGORIES:
        log.info(
            "%s: %d entries", CATEGORY_TITLES[category], len(entries_by_category[category])
        )

    existing_extra_by_category: dict[str, str] = {}
    preamble_by_category: dict[str, str | None] = {}
    for category in CATEGORIES:
        output_path = output_dir / CATEGORY_FILENAMES[category]
        existing_extra = extract_extra_section(output_path)
        existing_extra_by_category[category] = existing_extra
        preamble_by_category[category] = extract_preamble(output_path)
        warn_duplicate_urls(
            CATEGORY_FILENAMES[category], entries_by_category[category], existing_extra
        )

    if args.dry_run:
        log.info("Dry run: no files will be written.")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    for category in CATEGORIES:
        output_path = output_dir / CATEGORY_FILENAMES[category]
        content = render_category_file(
            category,
            entries_by_category[category],
            cited_in,
            existing_extra_by_category[category],
            preamble_by_category[category],
        )
        try:
            output_path.write_text(content, encoding="utf-8")
        except OSError as exc:
            log.error("Failed to write %s: %s", output_path, exc)
            return 1
        log.info("Wrote %s", output_path)

    return 0


def parse_args() -> argparse.Namespace:
    """Parse and return CLI arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Root of the HardwareifAI repository to scan (default: parent of scripts/)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to write papers.md/repositories.md/books.md/articles.md/"
        "courses.md into (default: <repo-root>/references)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report classification counts without writing any files",
    )
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(main(parse_args()))
