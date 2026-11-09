# One-Time Methodology

*Full methodology for every task performed once, at course creation; see [`curriculum_design_process.md`](curriculum_design_process.md) for the process overview these tasks belong to.*

## Professional profile definition

The curriculum starts from a fixed target, not from a syllabus: the specific professional abilities a learner must demonstrate by the end of the curriculum. This target is defined once, at course creation, and every later step, taxonomy scope, dependency graph, module design, works backward from it rather than forward from whatever topic feels foundational.

The abilities themselves are owned by [`vision/goals.md#learner-goals`](../vision/goals.md#learner-goals), not restated here. This task's role is to record that this definition happens first and once.

## Dependency graph seed chain

### Why a graph, not an index

This is arguably the single most important methodology decision in the whole project. The curriculum's backbone has to be a graph of prerequisites, not a flat list of topics: a flat list can be reordered arbitrarily without ever surfacing that one topic genuinely can't be understood before another. A graph makes that dependency explicit and checkable.

### Seed chain

The seed chain is the first version of the prerequisite graph, built once at course creation. The graph itself, and the reasoning behind each of its nodes and edges, live in [`taxonomy/dependency_graph.md`](../taxonomy/dependency_graph.md).

1. **Fix the terminal.** Take the end goal from the professional profile above and state it as the hardware the learner must be able to design. The graph has a single terminal: different workloads that hardware must serve are modelled as regimes feeding it (step 4), not as competing end goals.
2. **Derive backward.** Ask of each node "what must a learner already understand before this becomes designable?" and add each answer as a prerequisite node with an edge into it. Stop when a node presupposes nothing the curriculum itself would teach: that node is a root.
3. **Translate before connecting.** An edge from theory to hardware is admitted only through a quantifiable workload property that a hardware block can be sized against. A model family on its own states nothing about a chip; what it implies for compute, memory and communication does. Software layers enter the graph only where they are what actually reaches the hardware, and only at awareness level.
4. **Factor the shared substrate.** When several workload regimes need the same hardware, derive that hardware once as a shared node and isolate what differs into one regime node per workload, rather than duplicating parallel branches.
5. **Admit by reachability.** Every node must have a path to the terminal; a topic that cannot reach it is not preparatory to hardware design and does not belong on the graph.
6. **Record the derivation.** Write each backward derivation on the graph page as an explicit question-to-prerequisite table, one row per layer, so the reasoning behind every edge stays auditable after the fact.

Everything that happens to the graph afterward is a different cadence: it gets extended as the taxonomy and its recurring principles (see [`curriculum_design_process.md#topic-selection-framework`](curriculum_design_process.md#topic-selection-framework)) surface additional prerequisite relationships, and every topic that clears the fundamental-vs-fad rubric gets slotted into it with explicit prerequisites, per module, as described in [`per_module_methodology.md#dependency-graph-slotting`](per_module_methodology.md#dependency-graph-slotting). The graph is what actually determines module order in `curriculum/`, more than any single topic's perceived importance.

## Toolchain selection

At course creation, the curriculum commits once to a free/open-source toolchain (SystemVerilog as the primary HDL and verification language, plus one simulator, one synthesis tool, and one waveform viewer) before any module needs it, rather than letting each module improvise its own tools. Making that commitment well requires a genuine landscape survey against the project's own criteria.

These are the criteria the project has committed:

1. **Free and open-source, zero cost.** Hard constraint, not negotiable. Commercial tools are filtered out before they enter a role's candidate pool.
2. **Active maintenance.** A tool with a stalled or single-point-of-failure maintenance history is a risk to a project that runs for the full curriculum length.
3. **Community adoption and industry relevance.** Weighed against the job postings analyzed under [`quarterly_methodology.md#market-analysis-refresh`](quarterly_methodology.md#market-analysis-refresh) and against adoption in open-source projects, since job postings alone skew toward paid tools. Favor what the field actually uses and documents.
4. **Workflow fit.** Project design requires every module to ship RTL, a functional testbench with golden-reference comparison, and a synthesis check (see [`per_module_methodology.md#project-design`](per_module_methodology.md#project-design)); a tool that doesn't serve that specific loop cleanly is a poor fit regardless of its other merits.

Applying these four criteria against the full field of free/open-source alternatives, for each tool role in turn (RTL simulator, verification language and flow, synthesis tool, waveform viewer), is the actual one-time task. The full survey and its outcomes are an analysis artifact that live in [`analysis/toolchain/toolchain_selection.md`](../analysis/toolchain/toolchain_selection.md).

## Open items

None.
