# Paper Selection Criteria

*Defines the criteria used to select which academic papers anchor each module.*

## Why papers, not just models

The curriculum doesn't study models in isolation; it studies which ideas changed how hardware is built. This is a step that's commonly skipped in self-made study plans, and it shouldn't be: a model's headline result rarely explains what actually had to change in memory hierarchy, compute pattern, or communication to make that result practical. That change is what a hardware designer needs, and it's usually only visible in the paper itself, not in a summary of the model.

This is also principle 3 of [`vision/manifesto.md`](../vision/manifesto.md): "papers over tutorials". Every important concept in the curriculum is traced back to the scientific literature that introduced or established it, not to a secondary summary of it.

## Selection question

For every candidate paper or idea, the operating question is explicit and written down, not left implicit: "what does this innovation change for the hardware?" A paper only earns a place in the curriculum if that question has a concrete, hardware-relevant answer, not just a machine-learning-relevant one.

## Confirmed starting set

The confirmed set of papers/ideas already identified as having changed hardware, used as the seed list for paper analysis: Attention, FlashAttention, Mixture of Experts, Speculative Decoding, KV Cache, Diffusion, State Space Models, Mamba, RWKV, RetNet, Liquid Neural Networks, Vision Transformers, and Multimodal models. This list is expected to grow as the taxonomy (see [`topic_selection_framework.md`](topic_selection_framework.md)) surfaces additional families and as the field moves forward; it is a starting point, not a closed set.

## How a paper enters the curriculum

1. Identify the paper/idea, generally surfaced by the taxonomy, the market analysis (see [`industry_analysis.md`](industry_analysis.md)), or the dependency graph's prerequisite structure (see [`dependency_graph_methodology.md`](dependency_graph_methodology.md)).
2. Answer the selection question above in writing.
3. Run the fundamental-vs-fad rubric in [`topic_selection_framework.md`](topic_selection_framework.md) against the underlying idea, not the paper's specific named technique, so a paper that only demonstrates a fad doesn't earn a permanent module on that basis alone.
4. If it clears the rubric, write a full paper review using [`templates/paper_review.md`](../templates/paper_review.md) and cite it inline in the relevant module using the citation key already recorded in that review (author-plus-year keys, e.g. `[^vaswani2017]`), added to the module's own `## References` section.
5. Once cited anywhere in the repository, the paper is picked up automatically into the global bibliography at [`references/papers.md`](../references/papers.md) by `scripts/generate_bibliography.py`; it never needs to be added there by hand.

## Source reliability

Cite the paper's own primary source directly: the paper itself, its DOI, or its official publisher/archive page (e.g. arXiv), never a secondary encyclopedia entry about it.

## Open items

This page defines the selection question and the confirmed starting set grounded in the project's design reasoning so far. It does not yet define a minimum citation count, venue tier, or recency window as a hard filter; in practice, the fundamental-vs-fad rubric already does most of that filtering by proxy (an idea with no lasting hardware impact fails the rubric regardless of where it was published), but an explicit venue/quality bar may be worth adding once the paper set grows large enough to need one.
