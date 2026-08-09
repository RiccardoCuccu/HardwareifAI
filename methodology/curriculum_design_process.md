# Curriculum Design Process

*Describes the end-to-end process used to design and validate each curriculum module.*

## Why this process doesn't start from a syllabus

A self-made curriculum can easily default to mirroring how textbooks are ordered: machine learning first, then deep learning, then transformers, and so on. That ordering feels natural, but it isn't how companies actually hiring for AI-accelerator roles think. They reason from engineering problems outward, not from a syllabus.

Every step below, and the first-principles substitution test in particular (see [`topic_selection_framework.md`](topic_selection_framework.md)), exists specifically to keep the curriculum anchored to problems and market reality instead of drifting back into book-shaped topic ordering. This is also why the process is documented at all: see [`vision/manifesto.md`](../vision/manifesto.md) for why publishing the reasoning, not just the finished modules, is a core deliverable of this project.

## Process runs in parallel with learning, never as a gate

Methodology work and hands-on hardware learning run concurrently, not sequentially. A strict "finish the methodology, then start building" sequence defers all hands-on work until a large design document is finished, which can take months and kills momentum. There is no hard gate: the curriculum's guiding design document is a living artifact, developed alongside real module work, never a precondition for it.

The three broad milestone themes this repository is organised around (foundation, knowledge map, curriculum) are loose thematic groupings of content that mature concurrently, not a blocking sequence. Actual hardware learning, the first SystemVerilog project, and the design document's early sections all start in week one, in parallel.

## The 12-step process

The curriculum-design effort is treated as an engineering pipeline. These 12 steps are the throughline of the whole project:

1.  **Professional profile definition** - the target abilities the learner must demonstrate by the end of the curriculum; see [`vision/goals.md#learner-goals`](../vision/goals.md#learner-goals).
2.  **Market analysis** - recurring skills mined from public job postings, not books; see [`industry_analysis.md#market-analysis`](industry_analysis.md#market-analysis).
3.  **Paper analysis** - the criteria a paper must meet to enter the curriculum; see [`paper_selection_criteria.md`](paper_selection_criteria.md).
4.  **Hardware architecture analysis** - historical evolution of the field, folded into industry analysis; see [`industry_analysis.md#historical-evolution-why-the-field-builds-hardware-the-way-it-does`](industry_analysis.md#historical-evolution-why-the-field-builds-hardware-the-way-it-does).
5.  **AI taxonomy construction** - a map of modern AI wide enough to cover more than language models; see [`topic_selection_framework.md#stage-1-build-a-taxonomy-of-modern-ai-not-a-course-on-llms`](topic_selection_framework.md#stage-1-build-a-taxonomy-of-modern-ai-not-a-course-on-llms).
6.  **Core principles extraction** - the recurring ideas every module traces back to; see [`topic_selection_framework.md#stage-2-extract-the-recurring-principles`](topic_selection_framework.md#stage-2-extract-the-recurring-principles).
7.  **Dependency graph** - the prerequisite structure that determines module order; see [`dependency_graph_methodology.md`](dependency_graph_methodology.md).
8.  **Learning outcomes definition** - what a learner must demonstrate once a module is complete; see [`module_design_methodology.md#learning-outcomes-definition`](module_design_methodology.md#learning-outcomes-definition).
9.  **Module design** - assembling a module from the dependency graph and taxonomy into its `module_design.md`; see [`module_design_methodology.md#module-design`](module_design_methodology.md#module-design).
10. **Project design** - the hardware artifact that proves a module's competence was acquired; see [`project_design_methodology.md`](project_design_methodology.md).
11. **Validation** - self-verifiable evidence that a module's content was actually understood; see [`curriculum_maintenance.md#evaluation-metrics`](curriculum_maintenance.md#evaluation-metrics).
12. **Continuous update** - the two-speed maintenance model and cadence that keep the curriculum current; see [`curriculum_maintenance.md#continuous-update`](curriculum_maintenance.md#continuous-update).

Each numbered step above hands its output to the next: market analysis and paper analysis both feed the taxonomy and the fundamental-vs-fad rubric, which together produce the dependency graph, which determines module order, which in turn determines what each module's project has to prove.

## Personalising the process without forking it

Before profile definition (point 1 of the 12-step process above), a learner privately overlays their own starting point onto the public dependency graph, so their path skips what they already know and prioritises actual gaps. This overlay is a distinct, one-time step in the process, but it's about the graph, not about profile definition, so its full mechanics (what it marks, how it stays decoupled from the graph's own evolution, why results are never published) live in [`dependency_graph_methodology.md`](dependency_graph_methodology.md#the-graph-is-public-personal-paths-are-an-overlay-on-top-of-it).

## Open items

This process file grounds itself in the reasoning already captured for the curriculum's core steps. It does not yet define a template for logging progress against each of the 12 steps (e.g. a per-step status page); that tracking currently lives informally in GitHub Projects and Issues, per the repository's contribution workflow, and may warrant a dedicated artifact here once more modules exist.
