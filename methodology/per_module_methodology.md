# Per-Module Methodology

*How to carry out each task repeated for every new module; see [`curriculum_design_process.md`](curriculum_design_process.md) for where these tasks sit in the process and for the transversal concepts they apply.*

## Taxonomy population

The taxonomy is populated one family at a time, when the module covering that family is designed. Write the family's entry in whichever of [`taxonomy/ai_models_taxonomy.md`](../taxonomy/ai_models_taxonomy.md), [`taxonomy/hardware_taxonomy.md`](../taxonomy/hardware_taxonomy.md), or [`taxonomy/compute_patterns.md`](../taxonomy/compute_patterns.md) applies, answering the operating question defined in [`curriculum_design_process.md#stage-1-build-a-taxonomy-of-modern-ai-not-a-course-on-llms`](curriculum_design_process.md#stage-1-build-a-taxonomy-of-modern-ai-not-a-course-on-llms).

## Core principles mapping

Record, in the module's "Why this module exists" section, which confirmed recurring principles ([`curriculum_design_process.md#stage-2-extract-the-recurring-principles`](curriculum_design_process.md#stage-2-extract-the-recurring-principles)) the module's content connects back to. If the content recurs across families in a way no confirmed principle captures, flag it as a candidate for that list rather than treating it as a one-off.

## Paper analysis, per-topic anchor

Runs when a topic is about to become a module. Papers are studied rather than models alone, per principle 3 of [`vision/manifesto.md`](../vision/manifesto.md#the-curriculum-design-manifesto): what an idea forced to change in the hardware is usually visible only in the paper itself.

### Selection question

A paper earns a place only if both questions have a concrete written answer:

1. Does it trace back to a documented learner ability or job requirement ([`vision/goals.md#learner-goals`](../vision/goals.md#learner-goals), [`quarterly_methodology.md#market-analysis-refresh`](quarterly_methodology.md#market-analysis-refresh)), rather than being only academically interesting?
2. What does this innovation change for the hardware?

### How a paper enters the curriculum

1. Identify the candidate: from the taxonomy, the market analysis, the dependency graph, or the seed list in [`analysis/papers/`](../analysis/papers/README.md#seed-list).
2. Answer the selection question in writing.
3. Run the fundamental-vs-fad rubric ([`curriculum_design_process.md#stage-3-the-fundamental-vs-fad-rubric`](curriculum_design_process.md#stage-3-the-fundamental-vs-fad-rubric)) on the underlying idea, not on the paper's named technique.
4. If it clears the rubric, write a review with [`templates/paper_review_template.md`](../templates/paper_review_template.md) under [`analysis/papers/`](../analysis/papers/), citing the paper's primary source (the paper, its DOI, or its official archive page such as arXiv), and cite it in the module with its author-plus-year key (e.g. `[^vaswani2017]`). `scripts/generate_bibliography.py` adds it to [`references/papers.md`](../references/papers.md) automatically.

## Dependency graph slotting

Start from a competency surfaced by the market analysis instead of the terminal, and apply seed-chain steps 2-6 ([`one_time_methodology.md#seed-chain`](one_time_methodology.md#seed-chain)) until the derivation reaches the seed chain or a node already on the graph. Example: TPU architecture needs systolic arrays, which need tensor/MAC hardware, which needs general RTL fluency. Each node found this way is a candidate, slotted in only if it clears the fundamental-vs-fad rubric.

## Learning outcomes definition

Take from [`vision/goals.md#learner-goals`](../vision/goals.md#learner-goals) only the slice that the module's position on the graph actually advances, and write it in the module's `## Learning outcomes` section as a short, checkable list of demonstrable actions.

## Module design

A topic gets a module once it has cleared the rubric and has a slot with stated prerequisites on the graph. Fill in the module's `_module_design.md` from [`templates/module_template.md`](../templates/module_template.md) as follows:

- **Why this module exists**: why the topic earns a module, including the core principles it connects to (see Core principles mapping above).
- **Industry relevance** and **Job requirements**: the companies and recurring skills, citing a specific dated snapshot under [`analysis/industry/`](../analysis/industry/).
- **Scientific foundation**: the paper reviews under [`analysis/papers/`](../analysis/papers/) the content traces back to; if none exists yet, mark the field open rather than force-filling it.
- **Hardware implications**: the quantifiable workload properties the topic stresses ([`one_time_methodology.md#seed-chain`](one_time_methodology.md#seed-chain), step 3) and how they shape the project's PPA target. No fixed checklist.
- **Prerequisites**: the module's incoming edges on the graph, each with a one-line primer.
- **Projects**: the artifact, designed per Project design below.

Beside it, a Decision Log entry ([`templates/decision_log.md`](../templates/decision_log.md)) records only the decision itself: the alternatives considered and the fundamental-vs-fad scores. A topic that is rejected also gets an entry, stating why, and no module.

## Project design

For each topic, the design question is: "what is the smallest hardware artifact that proves this competence was acquired?". Only a hardware artifact counts, given the target sub-role in [`vision/target_audience.md`](../vision/target_audience.md) and principle 4 of [`vision/manifesto.md`](../vision/manifesto.md); an ML-only or software-only exercise does not. Projects grow along the ladder in [`vision/learning_philosophy.md`](../vision/learning_philosophy.md#learn-by-building-escalating-in-ambition).

### The hardware-artifact definition

Every project produces:

1. **RTL** implementing the module's concept.
2. **A testbench** checking the output against a golden reference in simulation, on the toolchain in [`one_time_methodology.md#toolchain-selection`](one_time_methodology.md#toolchain-selection).
3. **A PPA target**, stated before the work starts, for the figures the topic actually stresses (at least one), and the measured result against it. Any technique may be used to hit it.
4. **FPGA deployment**, optional, on a free/open toolchain.

When stated, each figure is measured this way:

- **Performance**: sustained throughput (results per cycle once the pipeline is full) and latency (cycles from an input to its result), measured in simulation and confirmed in the waveform; once synthesis is available, also a logic-depth budget (maximum logic levels between two registers) checked on the netlist, so a better cycle count can't hide a slower clock.
- **Area**: cell count reported by synthesis.
- **Power**: relative dynamic energy per result, i.e. net toggles while simulating the synthesised gate-level netlist over the testbench workload, divided by the results produced.

Worked example: Module 1, in [`curriculum/01-linear-algebra-tensor-operations/decision_log.md`](../curriculum/01-linear-algebra-tensor-operations/decision_log.md). Each project is written up with [`templates/project_template.md`](../templates/project_template.md) under [`projects/`](../projects/) and linked from the module's Projects section.

## Validation, per-module criteria

A module is complete when its project meets criterion (b) of [`curriculum_design_process.md#evaluation-metrics`](curriculum_design_process.md#evaluation-metrics) (zero mismatches against the golden reference and every stated PPA figure within budget), plus criterion (a) wherever a published result exists to reproduce. Criterion (c) never gates completion, per [`vision/learning_philosophy.md`](../vision/learning_philosophy.md#self-review-is-sufficient).

## Open items

- The power method is a provisional default: the toolchain has no dedicated power-estimation tool, so the toggle-count proxy is the simplest one it supports. Compare it against alternatives before the first module that states a power target.
- There is no shared default cell library or process assumption for area and power across projects; fix one once the first projects have been synthesised.
