# Curriculum Design Process

*Describes the end-to-end process used to build and keep the whole curriculum current: a defined start, at course creation, but by design no fixed end.*

## Why this process doesn't start from a syllabus

The process deliberately avoids textbook ordering, for the reason given in [`vision/manifesto.md#the-reframe`](../vision/manifesto.md#the-reframe).

Every step below, and the first-principles substitution test in particular (see Topic selection framework below), exists specifically to keep the curriculum anchored to problems and market reality instead of drifting back into book-shaped topic ordering. This is also why the process is documented at all: see [`vision/manifesto.md`](../vision/manifesto.md) for why publishing the reasoning, not just the finished modules, is a core deliverable of this project.

## Process runs in parallel with learning, never as a gate

Methodology work and hands-on hardware learning run concurrently, not sequentially. A strict "finish the methodology, then start building" sequence defers all hands-on work until a large design document is finished, which can take months and kills momentum. There is no hard gate: the curriculum's guiding design document is a living artifact, developed alongside real module work, never a precondition for it.

The three broad milestone themes this repository is organised around (foundation, knowledge map, curriculum) are loose thematic groupings of content that mature concurrently, not a blocking sequence. Actual hardware learning, the first SystemVerilog project, and the design document's early sections all start in week one, in parallel.

## The design process, by cadence

The curriculum-design effort is an engineering pipeline whose steps run on three different schedules: once at course creation, every quarter, or once per new module. It has a definite starting point, the one-time steps below, but by design no fixed end: the quarterly cadence keeps repeating for as long as the curriculum is maintained.

### One-time (built once, at course creation)

These three steps run once, at course creation, alongside the first module work rather than ahead of it, and produce the fixed scaffolding, the professional profile, the dependency graph's seed chain, and the toolchain, that every later cadence builds on. The taxonomy and the core recurring principles are not built upfront the same way: they're transversal concepts (see Topic selection framework below), populated incrementally as each module gets designed, not a one-time step of their own.

1. **Professional profile definition** - the target abilities the learner must demonstrate by the end of the curriculum; see [`one_time_methodology.md#professional-profile-definition`](one_time_methodology.md#professional-profile-definition).
2. **Dependency graph seed chain** - the initial prerequisite structure the graph grows from; see [`one_time_methodology.md#dependency-graph-seed-chain`](one_time_methodology.md#dependency-graph-seed-chain).
3. **Toolchain selection** - the free/open-source toolchain committed to once, before any module needs it; see [`one_time_methodology.md#toolchain-selection`](one_time_methodology.md#toolchain-selection).

### Quarterly (repeats every quarter, in the same sitting)

These three steps repeat every quarter, in the same sitting, since industry postings and emerging technology tend to move together; together they keep the curriculum's market signal and shipped portfolio current as the field moves.

1. **Market analysis refresh** - recurring skills re-mined from public job postings; see [`quarterly_methodology.md#market-analysis-refresh`](quarterly_methodology.md#market-analysis-refresh).
2. **Portfolio and graph validation** - re-checking the shipped portfolio, and the topic list and dependency graph, against a current job-postings sample; see [`quarterly_methodology.md#portfolio-and-graph-validation`](quarterly_methodology.md#portfolio-and-graph-validation).
3. **Technology Radar review** - reviewing the radar's rings and checking whether any thin-awareness topic now clears the fundamental-vs-fad rubric and should graduate into a full module; see [`quarterly_methodology.md#technology-radar-review`](quarterly_methodology.md#technology-radar-review).

### Per-module (repeats for every new module)

These eight steps repeat for every new module, turning the one-time scaffolding and the latest quarterly refresh into a specific module's design, project, and Decision Log entry.

1. **Taxonomy population** - filling in the new module's family entry in the taxonomy; see [`per_module_methodology.md#taxonomy-population`](per_module_methodology.md#taxonomy-population).
2. **Core principles mapping** - identifying which confirmed recurring principles the module connects back to; see [`per_module_methodology.md#core-principles-mapping`](per_module_methodology.md#core-principles-mapping).
3. **Paper analysis, per-topic anchor** - writing a module's specific paper anchor once that module needs it; see [`per_module_methodology.md#paper-analysis-per-topic-anchor`](per_module_methodology.md#paper-analysis-per-topic-anchor).
4. **Dependency graph slotting** - placing a new topic into the graph with explicit stated prerequisites; see [`per_module_methodology.md#dependency-graph-slotting`](per_module_methodology.md#dependency-graph-slotting).
5. **Learning outcomes definition** - what a learner must demonstrate once a module is complete; see [`per_module_methodology.md#learning-outcomes-definition`](per_module_methodology.md#learning-outcomes-definition).
6. **Module design** - assembling a module from the dependency graph and taxonomy into its `_module_design.md`; see [`per_module_methodology.md#module-design`](per_module_methodology.md#module-design).
7. **Project design** - the hardware artifact that proves a module's competence was acquired; see [`per_module_methodology.md#project-design`](per_module_methodology.md#project-design).
8. **Validation, per-module criteria** - self-verifiable evidence that a specific module's content was actually understood; see [`per_module_methodology.md#validation-per-module-criteria`](per_module_methodology.md#validation-per-module-criteria).

Each step hands its output on, across cadences: market analysis and paper analysis both feed the taxonomy and the fundamental-vs-fad rubric (see Topic selection framework below), which together produce the dependency graph, whose derivation mechanic is spelled out in [`per_module_methodology.md#dependency-graph-slotting`](per_module_methodology.md#dependency-graph-slotting), which determines module order, which in turn determines what each module's project has to prove. Market analysis and paper analysis also gate a module's design: its evidence fields cite the market-analysis snapshot and, where one exists, the paper review already in hand, not patched in afterward; see [`per_module_methodology.md#module-design`](per_module_methodology.md#module-design) for the mechanics.

## Topic selection framework

Topic selection runs in three stages: build a map of the field wide enough to actually cover modern AI (not just language models), extract what recurs across that map, then filter every candidate through a fundamental-vs-fad rubric before it earns a module. This section defines all three, as a transversal concept applied repeatedly across cadences (taxonomy and principles populated per module, the rubric applied per module and re-checked quarterly for graduation candidates), not a one-time step of its own; the taxonomy this framework produces is written up in [`taxonomy/ai_models_taxonomy.md`](../taxonomy/ai_models_taxonomy.md), [`taxonomy/hardware_taxonomy.md`](../taxonomy/hardware_taxonomy.md), and [`taxonomy/compute_patterns.md`](../taxonomy/compute_patterns.md), populated per [`per_module_methodology.md#taxonomy-population`](per_module_methodology.md#taxonomy-population).

### Stage 1: build a taxonomy of modern AI, not a course "on LLMs"

The curriculum has to cover modern AI as a whole, not narrow down to whichever family currently dominates public attention. The taxonomy spans: language models, vision, video, audio, robotics, reinforcement learning, diffusion, generative models, world models, agents, scientific AI, time series, biology, and graph neural networks.

For every family, the operating question is "what is the computational pattern?", not "what is the application domain?". Computational pattern is what actually matters to a hardware designer: two families with unrelated applications can share the same memory-traffic or parallelism profile, and that shared pattern is what belongs in the curriculum, not the application-level framing.

### Stage 2: extract the recurring principles

Once a family's taxonomy entry and its paper analysis (see [`per_module_methodology.md#paper-analysis-per-topic-anchor`](per_module_methodology.md#paper-analysis-per-topic-anchor)) exist, extract the ideas that recur across every family. These become the "trunk" of the curriculum: the load-bearing content every module eventually connects back to, per [`per_module_methodology.md#core-principles-mapping`](per_module_methodology.md#core-principles-mapping).

The confirmed recurring principles are: tensor operations, matrix multiplication, reductions, attention, memory movement, sparsity, communication, optimisation, and scheduling.

### Stage 3: the fundamental-vs-fad rubric

Not everything new lasts. Every candidate topic surfaced by market analysis (see [`quarterly_methodology.md#market-analysis-refresh`](quarterly_methodology.md#market-analysis-refresh)) has to clear this rubric before it enters the curriculum, so the curriculum can't drift into a buzzword checklist. Score each candidate against four criteria:

1. **Longevity/age** - has the underlying idea persisted across multiple hardware or model generations, or did it appear in the last 12-18 months only?
2. **Recurrence across model families** - does the concept show up in more than one family from the taxonomy (e.g. memory-traffic minimisation applies to LLMs, diffusion, and state space models alike), or is it specific to a single model or product?
3. **Survives a paradigm shift** - if the dominant architecture changed tomorrow, the way transformers superseded RNNs, would this topic still matter?
4. **Names a durable principle vs. a product/brand** - does the topic name a transferable principle (a parallel programming model, a memory hierarchy) or a specific named product/brand (a specific GPU model, a specific library version)?

A topic that fails criteria 3 and 4 is a fad or an implementation detail. It doesn't get its own module; it gets kept as a named example under whichever durable principle it instantiates, per the first-principles substitution test in [`vision/manifesto.md`](../vision/manifesto.md).

Worked examples, usable as the template for scoring new candidates:

- **Backpropagation**: passes all four criteria. Fundamental.
- **Transformer**: passes criteria 1-3, borderline on criterion 4 (it names an architecture, not a brand). Treated as fundamental.
- **Prompt engineering**: fails criteria 1, 3, and 4. Not fundamental relative to the curriculum's timeless-knowledge goal; at most a brief mention, never a dedicated module.

### Relationship to the dependency graph and to project design

A topic clearing this rubric doesn't automatically get a module: it still needs a place in the dependency graph (see [`per_module_methodology.md#dependency-graph-slotting`](per_module_methodology.md#dependency-graph-slotting)) and a hardware artifact that proves the competence was actually acquired (see [`per_module_methodology.md#project-design`](per_module_methodology.md#project-design)). Every topic decided on, included or rejected, gets a Decision Log entry, per [`per_module_methodology.md#module-design`](per_module_methodology.md#module-design).

## Validating the topic list and graph

The topic list and dependency graph are validated using public sources only (see the hard constraint in [`quarterly_methodology.md#public-sources-only`](quarterly_methodology.md#public-sources-only)). Two of the three channels below are entirely self-directed; the third depends on outside participation, which is never required (see [`vision/learning_philosophy.md`](../vision/learning_philosophy.md#self-review-is-sufficient)):

1. **Public expert content**: recorded conference talks, published interviews, engineer blog posts, and papers by people in hardware engineering, ML research, compiler engineering, ML systems, performance engineering, chip architecture, and software engineering roles, mined for the anchor question these sources implicitly answer: "what would a hiring manager expect a junior to already know?". Done as self-directed reading, this alone is sufficient validation. No fixed cadence: it runs whenever it runs.
2. **Public job postings**: the market scan in [`quarterly_methodology.md#market-analysis-refresh`](quarterly_methodology.md#market-analysis-refresh), used as self-directed triangulation against the graph and executed per [`quarterly_methodology.md#portfolio-and-graph-validation`](quarterly_methodology.md#portfolio-and-graph-validation).
3. **Community peer review**: made possible by publishing the graph and topic list openly through GitHub Issues and Discussions plus build-in-public posts, and treated as an optional bonus per [`vision/learning_philosophy.md`](../vision/learning_philosophy.md#self-review-is-sufficient); channels 1 and 2 alone fully validate the graph. One-on-one private expert interviews fall in the same category. No fixed cadence, same as channel 1.

## Evaluation metrics

"Did this work" is defined using evidence that's entirely self-verifiable (see [`vision/learning_philosophy.md`](../vision/learning_philosophy.md#self-review-is-sufficient)). Four metric types apply together, at two levels (per-module and portfolio-level): (a) and (b) are the only ones that ever gate a module's completion, (c) is optional, and (d) runs quarterly at portfolio level:

- **(a) Published-result reproduction**: for modules grounded in a specific paper or technique, reproduce a published benchmark or result as evidence the underlying concept was actually understood, not just read. Self-verifiable: the module owner compares their own result against the published one directly.
- **(b) Functional-test-plus-target pass**: every project must pass its own functional test suite and hit its stated power, performance and area (PPA) target, defined in [`per_module_methodology.md#project-design`](per_module_methodology.md#project-design). Passing tests alone, with no target met, doesn't count as complete.
- **(c) Community peer review**: an optional bonus signal that never gates any milestone, per [`vision/learning_philosophy.md`](../vision/learning_philosophy.md#self-review-is-sufficient).
- **(d) Periodic self-assessment against public job postings**: on the same quarterly cadence, re-check the portfolio against a current sample of public postings (see [`quarterly_methodology.md#portfolio-and-graph-validation`](quarterly_methodology.md#portfolio-and-graph-validation)). Self-verifiable: the module owner reads public postings and self-assesses directly.

How (a) and (b) combine into a module's pass criteria is defined in [`per_module_methodology.md#validation-per-module-criteria`](per_module_methodology.md#validation-per-module-criteria).

## Continuous update

The curriculum is kept current through the following mechanisms:

### Never "finished"

AI evolves too fast for a static curriculum to stay correct. The curriculum is never treated as a finished document; it's maintained on two different speeds, reviewed on a fixed cadence, and validated against evidence the module owner can check without depending on anyone else.

### Two-speed maintenance model

The curriculum splits into two layers, maintained differently, as introduced at the philosophy level in [`vision/learning_philosophy.md`](../vision/learning_philosophy.md):

- **Stable layer**: math foundations, architectures, systems, optimisation, hardware. Reviewed infrequently, because these don't need to change often.
- **Dynamic/emerging layer**: emerging models and techniques, kept at thin awareness only, meaning a brief mention plus Technology Radar tracking, never a dedicated project or deep-dive module unless and until a topic graduates to the stable layer via the fundamental-vs-fad rubric in Topic selection framework above.

A topic only moves from the dynamic layer to the stable layer by clearing that rubric, the same bar any new topic has to clear.

### Technology Radar

The curriculum maintains a continuously updated "AI Hardware Technology Radar" as a living artifact, presented explicitly as documented opinion rather than absolute truth, revised as part of the dynamic-layer review above. It's organised into four rings:

- **ADOPT**: technologies proven enough to build on now.
- **EXPLORE**: technologies worth active investigation, not yet adopted.
- **WATCH**: technologies too early to act on, kept on the radar for the next checkpoint.
- **DEPRECATED**: technologies superseded by later approaches, kept only as historical reference.

The current entries for each ring live in [`taxonomy/technology_radar.md`](../taxonomy/technology_radar.md), updated independently of this process description on the same quarterly cadence.

### Versioning

Curriculum changes, including a topic graduating from the dynamic to the stable layer, are logged as they happen in [`CHANGELOG.md`](../CHANGELOG.md), which defines the versioning scheme itself.

## Personalising the process without forking it

The generic, blank-slate dependency graph is a public artifact: the curriculum is meant to be reusable by other learners, so the graph itself stays learner-agnostic. Before profile definition (Professional profile definition, the first one-time step above), a learner privately overlays their own starting point onto it, so their path skips what they already know and prioritises actual gaps: a learner with professional RTL experience, such as the primary author (see [`vision/target_audience.md`](../vision/target_audience.md)), marks the foundational digital-design nodes as fast-review rather than full-study for that specific path, without changing what the public graph itself contains. Any learner using this curriculum runs the same overlay process once, privately, against their own baseline; the label results are never published, only the process is.

This overlay is a distinct, one-time methodological choice, not a task with its own schedule, and it's deliberately decoupled from the graph's own evolution: it's derived once, at the start, and then left alone. The public graph keeps being revised over time through the validation channels described above; there's no obligation to re-derive or reconcile a personal overlay every time the public graph changes, no named owner for keeping the two in sync, and no recurring cadence for it. Re-deriving an overlay is a deliberate, occasional choice if the public graph has drifted enough to warrant it, not a scheduled maintenance task.

## Open items

- No template yet for tracking progress on each step across the three cadences; it lives in GitHub Projects and Issues for now, and may get a dedicated artifact once more modules exist.
- No tie-breaking rule yet for topics that score ambiguously on criterion 4 of the fundamental-vs-fad rubric (architecture-level ideas too new to classify as durable or not); they are resolved case by case in the Decision Log until more candidates have gone through the rubric.
