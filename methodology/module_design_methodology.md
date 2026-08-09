# Module Design Methodology

*Describes how a module's learning outcomes are defined and how a module gets assembled once a topic earns its place in the curriculum.*

## Learning outcomes definition

The curriculum-wide learner abilities are already fixed in [`vision/goals.md#learner-goals`](../vision/goals.md#learner-goals): designing AI accelerators, understanding what modern models need from hardware, collaborating with ML researchers, reasoning about hardware/software trade-offs, translating a paper into a hardware requirement, optimising inference and training, and tracking the field without chasing every trend. Learning outcomes definition is the step that scopes that list down to size for a single module: not every module touches every learner-level ability, so a module's outcomes are the specific slice of that list its position on the dependency graph (see [`dependency_graph_methodology.md`](dependency_graph_methodology.md)) actually advances, phrased as demonstrable actions rather than restated wholesale.

Outcomes are recorded, not explained, inside the module's own `module_design.md`, using the `## Learning outcomes` section added to [`templates/module_template.md`](../templates/module_template.md) purely as the recording tool: a short, checkable list of what the learner should be able to do once the module is done. The concept itself is understood by working through the module's Scientific foundation and Hardware implications sections, not by reading the outcomes list; the outcomes list exists to state the target, not to teach toward it.

## Module design

A topic becomes eligible for its own module once it has cleared the fundamental-vs-fad rubric in [`topic_selection_framework.md#stage-3-the-fundamental-vs-fad-rubric`](topic_selection_framework.md#stage-3-the-fundamental-vs-fad-rubric) and has an explicit slot with stated prerequisites in the dependency graph (see [`dependency_graph_methodology.md`](dependency_graph_methodology.md)). Assembling the module means filling in the fixed section set defined by [`templates/module_template.md`](../templates/module_template.md) for that specific topic:

- **Industry relevance**: which companies from the market scan (see [`industry_analysis.md`](industry_analysis.md)) actually require this knowledge.
- **Job requirements**: which recurring skills, surfaced by the same market scan, the module covers.
- **Scientific foundation**: which papers, selected per [`paper_selection_criteria.md`](paper_selection_criteria.md), the module traces its content back to.
- **Hardware implications**: what changes for accelerators, using the same six-dimension lens (compute, memory, bandwidth, parallelism, communication, and power) the market analysis and later modules already use (see [`industry_analysis.md`](industry_analysis.md)).
- **Prerequisites**: the module's incoming edges on the dependency graph, each given a concise one-line primer per the template's standing documentation rule, not just listed as a bare assumption.
- **Projects**: the hardware artifact that proves the module's competence was actually acquired, designed per [`project_design_methodology.md`](project_design_methodology.md).

The repository has one worked instance of this process so far: [`curriculum/00-historical-context/_module_design.md`](../curriculum/00-historical-context/_module_design.md) (Module 0). It's a useful reference for tone and for how the Why/Scientific foundation/Hardware implications sections read once filled in, but it's an explicitly exempted, incomplete instance of the template rather than a fully representative example: it has no Prerequisites (documented as the first module, so none exist yet) and no Projects section fulfilled (documented as a deliberate exception, since it's the context-setting module that precedes any toolchain onboarding, with nothing yet to build against). Treat it as a partial precedent, not a template-complete worked example.

## Open items

Only Module 0 has gone through this process so far, and it's a structural exception on two of the template's sections rather than a representative case. This methodology page will need refining empirically, against a module that actually fills in Prerequisites and Projects, once more modules are built.
