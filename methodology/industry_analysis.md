# Industry Analysis

*Documents the recurring industry research used to keep the curriculum aligned with real job requirements.*

## Market analysis

Market analysis keeps the curriculum anchored to real hiring signal through the following:

### Start from companies, not books

Market analysis puts into practice the reasoning described in [`curriculum_design_process.md`](curriculum_design_process.md#why-this-process-doesnt-start-from-a-syllabus): it starts the topic list from engineering problems companies are actually solving, using public job postings only, not from how a book happens to sequence its material.

Hard constraint: this project is fully public and open-source, worldwide. No employer-internal material, process knowledge, or access of any kind is ever used or published here, or anywhere else in the curriculum. Any employer that happens to also appear in the public-postings sample below appears on the same footing as every other company; no internal advantage is used.

### How the market scan works

Collect public job postings from a deliberate mix of large players and startups. The starting sample, all sourced from public postings: NVIDIA, Google, Apple, Meta, Microsoft, Qualcomm and AMD among large players; Groq, Cerebras, Tenstorrent, Amazon Annapurna, Tesla AI, OpenAI Hardware, and Anthropic among startups and frontier labs.

Cluster the postings to find which skills recur constantly, which is what eliminates personal bias in what "feels" important. Example cluster of recurring skills already observed: Transformer, CUDA, Triton, PyTorch, Quantization, memory hierarchy, HBM, network-on-chip, compiler, scheduling, sparsity, tensor algebra.

Every candidate topic surfaced by this scan still has to clear the fundamental-vs-fad rubric in [`topic_selection_framework.md`](topic_selection_framework.md) before entering the curriculum. This step anchors market signal into the process; it doesn't turn the curriculum into a buzzword checklist on its own.

### Refresh cadence

The market scan is refreshed on a fixed quarterly cadence, not treated as a one-time snapshot. Public postings shift as the field moves, and a stale snapshot would silently reintroduce the exact bias (relying on what "feels" important instead of what's actually being hired for) this step exists to remove.

## Historical evolution: why the field builds hardware the way it does

Alongside the live market scan, the curriculum keeps a timeline of the field, not for nostalgia but because it explains why hardware today is built the way it is: CNN, then Transformer, then LLM, then Mixture of Experts, then reasoning models, then world models, then agentic AI, then test-time compute, with more transitions expected to follow.

For each transition in that timeline, later modules' own Hardware implications sections track how six dimensions changed: compute, memory, bandwidth, parallelism, communication, and power: power is a first-class dimension because it's the field's current binding constraint on scaling. Those same six dimensions are what the taxonomy's "computational pattern" question (see [`topic_selection_framework.md`](topic_selection_framework.md)) is built to capture for the current generation of models, so the historical timeline and the taxonomy stay consistent with each other rather than describing the field with two different vocabularies.

## Open items

The confirmed company sample and skill cluster above are a starting point, not a finished census; the actual quarterly refresh workflow (where the raw scan notes live, how cluster results get folded back into the dependency graph and Decision Log) is not yet fully specified here and should be fleshed out once the first refresh cycle actually runs.
