# Dependency Graph Methodology

*Describes how prerequisite relationships between modules are identified and structured.*

## Why a graph, not an index

This is arguably the single most important methodology decision in the whole project. The curriculum's backbone has to be a graph of prerequisites, not a flat list of topics: a flat list can be reordered arbitrarily without ever surfacing that one topic genuinely can't be understood before another. A graph makes that dependency explicit and checkable.

## Seed chain

The confirmed generic reference chain, used as the seed and extended as the taxonomy and its recurring principles (see [`topic_selection_framework.md`](topic_selection_framework.md)) surface additional prerequisite relationships:

```
Linear Algebra -> Tensor Algebra -> Autograd -> Neural Networks -> Attention -> Transformer -> LLM -> Quantization -> Inference -> Serving -> Accelerators
```

Every topic that clears the fundamental-vs-fad rubric gets slotted into this graph with explicit prerequisites, not just appended to the end of a list. The graph is what actually determines module order in `curriculum/`, more than any single topic's perceived importance.

## The graph is public; personal paths are an overlay on top of it

The generic, blank-slate dependency graph is a public artifact: the curriculum is meant to be reusable by other learners, so the graph itself stays learner-agnostic. A learner's personal starting point is layered on top of it as a one-time, private overlay, not folded into the public graph itself: for the primary author, professional RTL design, simulation, and verification experience already covers foundational digital-design concepts, so that overlay marks those nodes as fast-review rather than full-study for that specific path, without changing what the public graph itself contains. Any learner using this curriculum runs the same overlay process once, privately, against their own baseline; the label results are never published, only the process is.

This overlay is deliberately decoupled from the graph's own evolution: it's derived once, at the start, and then left alone. The public graph keeps being revised over time through the validation channels below; there's no obligation to re-derive or reconcile a personal overlay every time the public graph changes, no named owner for keeping the two in sync, and no recurring cadence for it. Re-deriving an overlay is a deliberate, occasional choice if the public graph has drifted enough to warrant it, not a scheduled maintenance task. See [`curriculum_design_process.md`](curriculum_design_process.md#personalising-the-process-without-forking-it) for where this overlay step sits relative to the rest of the 12-step process.

## Validating the graph and topic list

Because the project is fully public with no employer-internal channel of any kind, the topic list and dependency graph are validated using public sources, not private access. Two of the three channels below are entirely self-directed and need no external party to respond to anything; the third is a welcome bonus signal if it happens, never a required or awaited one, since the repository may realistically see zero external interaction across the whole project:

1. **Public expert content**: recorded conference talks, published interviews, engineer blog posts, and papers by people in hardware engineering, ML research, compiler engineering, ML systems, performance engineering, chip architecture, and software engineering roles, mined for the anchor question these sources implicitly answer: "what would a hiring manager expect a junior to already know?" Done as self-directed reading, this alone is sufficient validation.
2. **Public job postings**: the same market scan described in [`industry_analysis.md`](industry_analysis.md), used here as ongoing self-directed triangulation against the graph, re-checked periodically rather than treated as a one-time snapshot.
3. **Community peer review**, an optional bonus signal only: made possible by publishing the graph and topic list openly through GitHub Issues and Discussions plus build-in-public posts, but never solicited, chased, or waited for. If it happens, it's a genuinely welcome addition to channels 1 and 2. If it never happens across the entire project, the graph and topic list remain fully validated by 1 and 2 alone. One-on-one private expert interviews are the same kind of secondary, best-effort, opportunistic signal, never a primary validator or a blocking dependency for any step.

## Open items

The seed chain above is deliberately generic and linear; the actual graph, once real modules exist, will have branching and cross-family prerequisites (e.g. a diffusion-specific node depending on a shared "memory movement" node rather than on the LLM branch directly) that this page doesn't yet enumerate. A concrete graph-representation format (which file, which structure) for `taxonomy/` still needs to be decided as the first few modules are built out.
