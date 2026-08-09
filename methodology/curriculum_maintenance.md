# Curriculum Maintenance

*Describes how the curriculum is kept current as the field evolves.*

## Evaluation metrics

"Did this work" is defined using evidence that's entirely self-verifiable, since the project has no employer-internal channel to draw on and has to fully succeed even with zero external interaction. Four metric types apply together, at two levels (per-module and portfolio-level); only the first three are ever required:

- **(a) Published-result reproduction**: for modules grounded in a specific paper or technique, reproduce a published benchmark or result as evidence the underlying concept was actually understood, not just read. Self-verifiable: the module owner compares their own result against the published one directly.
- **(b) Functional-test-plus-target pass**: every project must pass its own functional test suite and hit its stated performance, area, or throughput target, defined in [`project_design_methodology.md`](project_design_methodology.md). Passing tests alone, with no target met, doesn't count as complete.
- **(c) Community peer review**, optional bonus signal only: self-review is the default and fully sufficient path for every milestone. External review, if it happens, adds confidence beyond the self-review baseline; it's never required, never solicited on a mandatory timeline, and its absence never blocks, weakens, or delays any milestone.
- **(d) Periodic self-assessment against public job postings**: on the same quarterly cadence, re-check the portfolio against a current sample of public postings (see [`industry_analysis.md`](industry_analysis.md)). Self-verifiable: the module owner reads public postings and self-assesses directly.

Per-module pass criteria: a module is complete when (b) is satisfied and (a) is satisfied wherever a published result exists to reproduce, both purely self-verified. (c) never gates completion; a self-review documented in the module write-up is enough.

## Continuous update

The curriculum is kept current through the following mechanisms:

### Never "finished"

AI evolves too fast for a static curriculum to stay correct. The curriculum is never treated as a finished document; it's maintained on two different speeds, reviewed on a fixed cadence, and validated against evidence the module owner can check without depending on anyone else.

### Two-speed maintenance model

The curriculum splits into two layers, maintained differently, as introduced at the philosophy level in [`vision/learning_philosophy.md`](../vision/learning_philosophy.md):

- **Stable layer**: math foundations, architectures, systems, optimisation, hardware. Reviewed infrequently, because these don't need to change often.
- **Dynamic/emerging layer**: emerging models and techniques, kept at thin awareness only, meaning a brief mention plus Technology Radar tracking, never a dedicated project or deep-dive module unless and until a topic graduates to the stable layer via the fundamental-vs-fad rubric in [`topic_selection_framework.md`](topic_selection_framework.md).

A topic only moves from the dynamic layer to the stable layer by clearing that rubric, the same bar any new topic has to clear; there's no separate, lighter promotion path for topics that are already being tracked at thin awareness.

### Quarterly checkpoint

The dynamic layer is reviewed on the same fixed quarterly cadence as the market-signal refresh in [`industry_analysis.md`](industry_analysis.md), in the same sitting, since industry postings and emerging technology tend to move together. Each quarterly checkpoint covers:

- Re-scanning public job postings for new recurring skills (see [`industry_analysis.md`](industry_analysis.md)).
- Reviewing the Technology Radar's ADOPT/EXPLORE/WATCH/DEPRECATED rings and moving entries between rings as evidence accumulates.
- Checking whether any thin-awareness topic now clears the fundamental-vs-fad rubric and should graduate into a full module.
- Re-reading a current sample of public AI-accelerator job postings against the shipped portfolio, to catch any gap against current requirements for the target sub-role (see criterion (d) above).

### Technology Radar

The curriculum maintains a continuously updated "AI Hardware Technology Radar" as a living artifact, presented explicitly as documented opinion rather than absolute truth, revised as part of the dynamic-layer review above. It's organised into four rings, with the confirmed starting entries:

- **ADOPT**: Tensor Cores, Transformer accelerators, Quantization.
- **EXPLORE**: Photonic computing, Analog AI, Neuromorphic.
- **WATCH**: Quantum ML, New architectures.
- **DEPRECATED**: Old approaches.

### Versioning

Curriculum changes, including a topic graduating from the dynamic to the stable layer, are logged as they happen in [`CHANGELOG.md`](../CHANGELOG.md), which defines the versioning scheme itself.

## Open items

The exact home for the Technology Radar as a standalone page (alongside `methodology/` or `taxonomy/`, per the repository's placement notes) is not yet created; this page describes its four rings and starting entries, sourced directly from the project's existing design reasoning, but the radar itself should be split out into its own file once it needs to be updated independently of this maintenance process description.
