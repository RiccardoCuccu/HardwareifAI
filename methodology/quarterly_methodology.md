# Quarterly Methodology

*How to carry out each task repeated every quarter, in the same sitting; see [`curriculum_design_process.md`](curriculum_design_process.md) for where these tasks sit in the process and for the transversal concepts they apply.*

## Market analysis refresh

The topic list starts from the problems companies are hiring to solve, not from how a book sequences its material (see [`curriculum_design_process.md`](curriculum_design_process.md#why-this-process-doesnt-start-from-a-syllabus)).

### Public sources only

Hard constraint: only public job postings are used. No employer-internal material, process knowledge or access of any kind is ever used or published anywhere in the curriculum, and any employer that appears in the sample is treated like every other company.

### How the market scan works

1. **Sample companies**: a deliberate mix of large players and startups.
2. **Select postings**: keep only postings that require hands-on RTL/chip-design work and are scoped to AI-accelerator hardware.
3. **Record each posting**: one record per posting with [`templates/job_posting_template.md`](../templates/job_posting_template.md), plus an HTML snapshot of the original page, under `analysis/industry/<quarter>/job_posts/`.
4. **Cluster the skills**: count, for each skill, how many selected postings mention it (postings, not keyword hits). This counting is what removes personal bias about what "feels" important.
5. **Write the snapshot**: a new dated file `analysis/industry/<quarter>/<quarter>.md` with [`templates/industry_analysis_template.md`](../templates/industry_analysis_template.md). Earlier snapshots are kept, never overwritten; a module's design cites the snapshot(s) that were current when it was designed.

Candidate topics surfaced by the scan then go through the fundamental-vs-fad rubric ([`curriculum_design_process.md#stage-3-the-fundamental-vs-fad-rubric`](curriculum_design_process.md#stage-3-the-fundamental-vs-fad-rubric)).

## Portfolio and graph validation

Against the new snapshot, check two things and record the outcome in the snapshot's "Portfolio and graph check" field:

- **Portfolio**: whether the shipped projects still cover what the target sub-role is hired for (criterion (d) of [`curriculum_design_process.md#evaluation-metrics`](curriculum_design_process.md#evaluation-metrics)).
- **Topic list and graph**: map every skill in the cluster to a node on the dependency graph, or mark it out of scope with a link to the decision that excludes it. A skill with no node is a candidate competency: run [`per_module_methodology.md#dependency-graph-slotting`](per_module_methodology.md#dependency-graph-slotting) from it, then the fundamental-vs-fad rubric. This is the job-postings channel of [`curriculum_design_process.md#validating-the-topic-list-and-graph`](curriculum_design_process.md#validating-the-topic-list-and-graph).

## Technology Radar review

In [`taxonomy/technology_radar.md`](../taxonomy/technology_radar.md), applying the concepts in [`curriculum_design_process.md#continuous-update`](curriculum_design_process.md#continuous-update):

- Move entries between rings as evidence accumulates.
- Check whether any thin-awareness topic now clears the fundamental-vs-fad rubric and should graduate into a full module; log any graduation in [`CHANGELOG.md`](../CHANGELOG.md).

## Open items

None.
