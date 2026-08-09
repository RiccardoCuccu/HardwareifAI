# Topic Selection Framework

*Defines the criteria used to decide which topics earn a place in the curriculum.*

Topic selection runs in three stages: build a map of the field wide enough to actually cover modern AI (not just language models), extract what recurs across that map, then filter every candidate through a fundamental-vs-fad rubric before it earns a module. This page defines all three. The taxonomy this stage produces is written up in [`taxonomy/ai_models_taxonomy.md`](../taxonomy/ai_models_taxonomy.md), [`taxonomy/hardware_taxonomy.md`](../taxonomy/hardware_taxonomy.md), and [`taxonomy/compute_patterns.md`](../taxonomy/compute_patterns.md); this page defines the method behind those pages, not their content.

## Stage 1: build a taxonomy of modern AI, not a course "on LLMs"

The curriculum has to cover modern AI as a whole, not narrow down to whichever family currently dominates public attention. The taxonomy spans: language models, vision, video, audio, robotics, reinforcement learning, diffusion, generative models, world models, agents, scientific AI, time series, biology, and graph neural networks.

For every family, the operating question is "what is the computational pattern?", not "what is the application domain?" Computational pattern is what actually matters to a hardware designer: two families with unrelated applications can share the same memory-traffic or parallelism profile, and that shared pattern is what belongs in the curriculum, not the application-level framing.

## Stage 2: extract the recurring principles

Once the taxonomy and the paper analysis (see [`paper_selection_criteria.md`](paper_selection_criteria.md)) are collected, extract the ideas that recur across every family. These become the "trunk" of the curriculum: the load-bearing content every module eventually connects back to.

The confirmed recurring principles are: tensor operations, matrix multiplication, reductions, attention, memory movement, sparsity, communication, optimisation, and scheduling.

## Stage 3: the fundamental-vs-fad rubric

Not everything new lasts. Every candidate topic surfaced by market analysis (see [`industry_analysis.md`](industry_analysis.md)) has to clear this rubric before it enters the curriculum, so the curriculum can't drift into a buzzword checklist. Score each candidate against four criteria:

1. **Longevity/age** - has the underlying idea persisted across multiple hardware or model generations, or did it appear in the last 12-18 months only?
2. **Recurrence across model families** - does the concept show up in more than one family from the taxonomy (e.g. memory-traffic minimisation applies to LLMs, diffusion, and state space models alike), or is it specific to a single model or product?
3. **Survives a paradigm shift** - if the dominant architecture changed tomorrow, the way transformers superseded RNNs, would this topic still matter?
4. **Names a durable principle vs. a product/brand** - does the topic name a transferable principle (a parallel programming model, a memory hierarchy) or a specific named product/brand (a specific GPU model, a specific library version)?

A topic that fails criteria 3 and 4 is a fad or an implementation detail. It doesn't get its own module; it gets kept as a named example under whichever durable principle it instantiates, per the first-principles substitution test in [`vision/manifesto.md`](../vision/manifesto.md).

Worked examples, usable as the template for scoring new candidates:

- **Backpropagation**: passes all four criteria. Fundamental.
- **Transformer**: passes criteria 1-3, borderline on criterion 4 (it names an architecture, not a brand). Treated as fundamental.
- **Prompt engineering**: fails criteria 1, 3, and 4. Not fundamental relative to the curriculum's timeless-knowledge goal; at most a brief mention, never a dedicated module.

## Relationship to the dependency graph and to project design

A topic clearing this rubric doesn't automatically get a module: it still needs a place in the dependency graph (see [`dependency_graph_methodology.md`](dependency_graph_methodology.md)) and a hardware artifact that proves the competence was actually acquired (see [`project_design_methodology.md`](project_design_methodology.md)). Every topic that does clear the rubric and gets a module gets a Decision Log entry recording why it was included, why alternatives were rejected, and which project demonstrates it, per [`templates/decision_log.md`](../templates/decision_log.md).

## Open items

This framework does not yet define a tie-breaking rule for topics that score ambiguously on criterion 4 (architecture-level ideas that are new enough to be hard to classify as durable or not). In practice this is resolved case by case and logged in the Decision Log; a sharper rule may be worth adding once more real candidates have gone through the rubric.
