# HardwareifAI Curriculum Roadmap — Skeleton (Draft v1)

This is a first-pass structural skeleton for the actual curriculum content (Module 1, Module 2, Module 3, and so on). It is explicitly NOT a locked syllabus: module boundaries, ordering within a module, and hour allocation are all expected to shift as the project's own validation process (public expert signal, job-posting analysis, any community peer review that happens to arrive) and its quarterly market-signal and emerging-layer checkpoint surface corrections. Treat every rationale below as a first draft of that module's future decision-log entry, not the final version.

## Scope discipline

This skeleton deliberately does NOT attempt to cover all of modern AI. It selects only the topics that pass the project's fundamental-vs-fad rubric and sit on the confirmed dependency-chain seed — Linear Algebra, Tensor Algebra, Autograd, Neural Networks, Attention, Transformer, LLM, Quantization, Inference, Serving, Accelerators — or its direct extensions (MoE, sparsity, KV-cache management, memory hierarchy, scheduling). Everything else is pushed to the "explicitly deferred to thin-awareness only" list at the end.

## Standing rules applied to every module below (not repeated per-module for brevity)

- Every module gets its own dedicated, numerically-prefixed folder under `curriculum/` (e.g. `curriculum/02-linear-algebra-tensor-operations/`) — one module per folder, no sharing between modules.
- Every module (except Section 0) gets a `module_design.md` file following the project's standard module template, including a Prerequisites section where every prerequisite receives a concise one-line primer stating what the assumed concept is — not written out here, only flagged as required.
- Every module's Projects section must satisfy the project's hardware-artifact definition: SystemVerilog RTL, a free-toolchain testbench (SystemVerilog + Verilator by default; see Module 11 for the single cocotb exception), and a stated performance/area/throughput target checked at the end. ML-only or software-only exercises do not count.
- Foundational RTL/verification-methodology modules stay in the public generic curriculum even though a learner with strong prior RTL/verification background (per this project's personalized-overlay approach) may skip most of them — this is called out per-module where it applies, so foundational content is never silently stripped for other learners.

## Explicitly out of scope by design

Two topic areas are deliberately excluded from this curriculum, not merely unaddressed: physical design (place-and-route, timing closure, and related back-end implementation flow) and power/DVFS optimization. The target role this curriculum trains for is RTL and microarchitecture design specifically, not physical design or power engineering; both are real, adjacent disciplines that a graduate of this curriculum would hand off to a different specialist role. This boundary is stated explicitly here so it reads as a deliberate scope decision, not a gap nobody noticed.

---

## Section 0: Historical Context — From Parallel Computing to AI Accelerators

The only section exempt from the hardware-artifact exercise requirement that governs every other section below: it is narrative and context-setting, with no attached project.

Covers, concisely: the general-computing and parallel-computing lineage that feeds into today's AI accelerators (vector processors, GPUs as the first mass-market parallel accelerator, the shift from general-purpose to domain-specific hardware); then the model-family timeline — CNN, Transformer, LLM, MoE, Reasoning models, World Models, Agentic AI, test-time compute — walked transition by transition through five dimensions: compute, memory, bandwidth, parallelism, communication. The goal is a mental model of WHY hardware looks the way it does today (e.g. why HBM and interconnect bandwidth became the binding constraint once LLMs made attention memory-bound, why MoE reintroduced dynamic routing and communication concerns general-purpose accelerators weren't originally built for), not a trivia timeline.

**Folder:** `curriculum/00-historical-context/`

Lives as an introductory reading, since it precedes and motivates every later module's "why this hardware pattern matters" framing but produces no standalone project of its own.

**Prerequisite:** none — entry point for every learner, regardless of prior RTL/verification background.

---

## Module 1: Digital Design, Verification & Toolchain Foundations

**Folder:** `curriculum/01-digital-design-verification-toolchain-foundations/`

**Rationale:** Every later module assumes fluency with RTL description, testbench-based verification, and the project's specific free toolchain (SystemVerilog, Verilator, Yosys, GTKWave). This module is the on-ramp into that toolchain and into simulation-driven verification as a discipline, for any learner who does not already have it.

**This module is untimed and self-paced, not part of the weeks-1-4 clock.** It sits before Module 2 in sequence, but a learner works through it at their own pace, for however long it genuinely takes, which varies widely by starting point. It does not count against the weeks-1-4 window for a learner who can skip it, because it is conditionally skipped rather than universally required: a learner who already has RTL design and simulation/verification experience — professional or otherwise — skips this module entirely per the personalized-overlay approach and moves straight to Module 2. The weeks-1-4 clock (see Module 2 below) starts only once RTL/toolchain fluency exists, whether that fluency comes from completing this module or from prior experience.

Required in full only for the generic learner without that fluency; skippable for RTL-strong learners per the personalized-overlay principle.

**Example artifact:** an 8-bit pipelined ALU (add/sub/shift/compare) with a SystemVerilog testbench run via Verilator, checked against a golden model, with a stated pipeline-latency target confirmed in GTKWave and a Yosys synthesis pass with no errors. This artifact is a foundational competence check, not the weeks-1-4 escalation artifact — that role belongs to Module 2 alone.

**Prerequisite:** none (entry point for a learner without prior RTL/verification fluency). Primer treatment applies once real content is drafted — none needed at skeleton stage.

---

## Module 2: Linear Algebra & Tensor Operations in Hardware

**Folder:** `curriculum/02-linear-algebra-tensor-operations/`

**Rationale:** Opens the dependency-chain seed (Linear Algebra to Tensor Algebra) and the two most load-bearing trunk principles: tensor operations and matrix multiplication. **This module alone owns the weeks-1-4 window and its target artifact** — a MAC (multiply-accumulate) unit that grows into a small systolic array — exactly as defined in the project's execution plan; Module 1 is a separate, untimed on-ramp that precedes this window for learners who need it, not part of it. The systolic-array design also requires an explicit dataflow choice — weight-stationary, output-stationary, or row-stationary — and the module's artifact must state and justify which one it uses, since this is a first-order hardware design decision for any real systolic array, not an implementation detail. Builds the single most reused hardware building block in the rest of the curriculum.

**Example artifact:** a 4x4 int8 systolic-array MAC block, SystemVerilog RTL, Verilator testbench against a golden matrix-multiply reference (reset, pipeline fill/drain, back-to-back streaming), 1 output/cycle sustained-throughput target once full, Yosys area budget, GTKWave-confirmed pipeline latency, with a stated and justified dataflow choice (weight-stationary, output-stationary, or row-stationary).

**Prerequisite:** RTL/toolchain fluency, via Module 1 or prior experience. Primer needed: linear algebra basics (vectors, matrix multiplication) — picked up just-in-time, not as an upfront block.

---

## Module 3: Computational-Pattern Awareness — ML, Autograd & Reductions

**Folder:** `curriculum/03-computational-pattern-awareness/`

**Rationale:** Awareness-level only, per the hardware-first/software-aware principle — not ML-engineer depth. Introduces what a tensor computation and autograd actually are as computational patterns, and lands the "reductions" trunk principle, which recurs across nearly every AI model family (pooling, normalization, loss aggregation, softmax denominators).

**Prerequisite:** Module 2 should have shipped by month 3 under the standard sequence; if it has not, Module 3 begins anyway in parallel with the still-in-progress Module 2, per the hard month-3 deadline override already defined in the project's execution plan — this module's schedule is subordinate to that deadline, not the other way around.

**Example artifact:** a configurable tree-reduction unit in SystemVerilog (parameterizable sum/max reduction over a streamed vector, the hardware primitive behind pooling, normalization, and loss reduction), verified against a golden reduction result with a stated cycles-per-N-element throughput target.

**Primer needed:** gradient descent and autograd as concepts (what is being reduced/accumulated and why), kept strictly conceptual.

---

## Module 4: Neural Network Building Blocks in Hardware

**Folder:** `curriculum/04-neural-network-building-blocks/`

**Rationale:** Continues the dependency chain (Autograd to Neural Networks) at awareness level: dense/fully-connected layers, activation functions, and why these specific operations (matmul plus bias plus nonlinearity) are the atomic hardware pattern every deeper architecture composes. First module where a full micro-datapath (compute plus activation) is assembled from Module 2 and Module 3 primitives, previewing the composition pattern reused in Module 5 and Module 12.

**Example artifact:** a fully-connected-layer accelerator tile — MAC array (reusing Module 2's block) plus bias add plus ReLU activation LUT — in SystemVerilog, verified against a NumPy-generated golden reference, with a stated layer-throughput (outputs/cycle) target.

**Prerequisite:** Module 2 (tensor/MAC hardware), Module 3 (computational-pattern awareness). Primer needed: perceptron/MLP structure, common activation functions (ReLU, sigmoid) at a one-line conceptual level.

---

## Module 5: Attention & Transformer Microarchitecture

**Folder:** `curriculum/05-attention-transformer-microarchitecture/`

**Rationale:** The dependency chain's next link (Neural Networks to Attention to Transformer) and the point where two more trunk principles enter directly: attention and memory movement. Arguably the highest-leverage module for the target role, since attention's memory-bound behavior is the single biggest driver of modern AI-accelerator microarchitecture decisions. Kept at hardware-translation depth: what softmax and QKV scoring demand of a datapath and memory system, not transformer research.

**Example artifact:** a scaled dot-product attention core (QK^T score computation, softmax unit, weighted-value accumulation) for a small fixed tile size, in SystemVerilog, verified against a golden attention-output reference, with a stated cycles-per-token throughput target.

**Prerequisite:** Module 4 (NN building blocks), Module 2 (MAC/tensor core reused inside the attention datapath). Primer needed: transformer architecture at a conceptual level (QKV, softmax, one paragraph), not the full original attention paper.

---

## Module 6: Memory Hierarchy & On-Chip Communication

**Folder:** `curriculum/06-memory-hierarchy-on-chip-communication/`

**Rationale:** Lands the trunk's memory-movement and communication principles as first-class hardware topics, directly motivated by Module 5's attention core being memory-bound. Covers SRAM/HBM hierarchy trade-offs and basic on-chip interconnect concepts. On-chip interconnect design is a recurring, explicitly named hiring-signal skill for this target role, so this module's artifact now covers arbitration/interconnect directly rather than leaving it as a named-but-unbuilt topic.

**Example artifact:** a double-buffered SRAM scratchpad controller with DMA-style streaming (ping-pong buffers feeding Module 5's attention core without stalling), plus a basic round-robin arbiter/crossbar for multi-port access, in SystemVerilog, verified for a stated sustained-bandwidth (bytes/cycle) target with no read/write hazards and fair arbitration across ports.

**Prerequisite:** Module 5 (motivates why memory movement matters for a real workload). Primer needed: cache/SRAM basics, compute-bound vs. memory-bound as a concept, basic arbitration concepts (round-robin fairness).

---

## Module 7: Sparsity & MoE Routing Hardware

**Folder:** `curriculum/07-sparsity-moe-routing/`

**Rationale:** Continues the dependency chain (Transformer to LLM) and lands the trunk's sparsity principle, plus Mixture-of-Experts dynamic routing as a first-class hardware topic in its own right — both, at awareness level, are why LLM-scale serving demands hardware support that dense-only accelerators lack. Now carries two dedicated artifact components rather than a single sparsity-only build, so MoE routing is proven with hardware, not just described.

**Example artifact:** the sparsity-aware MAC unit with zero-operand gating/skip logic, plus a simple N-way expert-dispatch router (combinational or sequential compare-and-select logic routing an input token to 1-of-N expert compute blocks based on a routing score), both in SystemVerilog, verified against a dense baseline with a stated energy/cycle-reduction target.

**Prerequisite:** Module 5 (attention/transformer), Module 6 (memory hierarchy). Primer needed: MoE routing at a conceptual level (why dynamic expert selection exists, what it costs in communication).

---

## Module 8: KV-Cache & Memory Management Hardware

**Folder:** `curriculum/08-kv-cache-memory-management/`

**Rationale:** Isolates KV-cache and memory-management hardware as its own topic, distinct from Module 7's compute-side sparsity and routing work, because eviction/paging logic is a materially different design problem (a memory controller and datapath, not a compute datapath). Builds directly on Module 6's scratchpad/memory-hierarchy work and feeds the attention core built in Module 5, closing the gap where KV-cache was previously described only at awareness level with no artifact proving the competence.

**Example artifact:** a KV-cache controller block (circular-buffer or paged-style cache with a stated eviction policy), feeding into the attention core / scratchpad pattern from Modules 5 and 6, in SystemVerilog, verified for correct eviction behavior with a stated cache-hit-rate or access-latency target.

**Prerequisite:** Module 5 (attention core the cache feeds), Module 6 (scratchpad/memory-hierarchy pattern reused). Primer needed: KV cache purpose (why it exists, what it trades off), basic eviction-policy concepts.

---

## Module 9: Quantization & Numerical Optimization

**Folder:** `curriculum/09-quantization-numerical-optimization/`

**Rationale:** The dependency chain's next explicit node (LLM to Quantization) and the trunk's optimization principle. Awareness of int8/mixed-precision numerics and why reduced precision is one of the highest-leverage hardware/software co-design levers for both inference cost and area. Placed after the LLM-scale modules, not before Module 2, since quantization only makes sense once there is a concrete matmul/attention workload to compress.

**Example artifact:** a configurable int8 requantization block (scale plus zero-point) in SystemVerilog, verified against a golden quantized reference, with a stated area budget under Yosys synthesis.

**Prerequisite:** Module 2 (tensor/MAC core being quantized), Module 7 (realistic LLM-scale workload context). Primer needed: fixed-point arithmetic and quantization-aware training as concepts — also a natural trigger point for a just-in-time C/math refresh.

---

## Module 10: Inference, Scheduling & Serving-Aware Accelerator Design

**Folder:** `curriculum/10-inference-scheduling-serving/`

**Rationale:** Closes out the dependency chain's final links (Inference to Serving to Accelerators) and the trunk's scheduling principle. Covers how serving-level concerns — batching, pipelining, continuous request scheduling, and KV-cache pressure under sustained load — shape microarchitecture-level control logic, not just the compute datapaths built in earlier modules. Ties Modules 6 through 9's building blocks into something that behaves like an actual accelerator subsystem under sustained load, directly preparing for the Module 12 capstone.

**Example artifact:** a pipelined tile-scheduler/controller issuing work to Module 2's systolic array with double-buffered inputs (Module 6's scratchpad pattern reused), verified for a stated sustained-throughput target under back-to-back, variable-sized requests with no pipeline bubbles.

**Prerequisite:** Module 6 (memory hierarchy), Module 7 (sparsity/MoE routing), Module 8 (KV-cache management, since serving-level scheduling directly interacts with KV-cache pressure under load), Module 9 (quantized datapath being scheduled). Primer needed: pipelining/scheduling basics, speculative decoding as a one-line concept.

---

## Module 11: Verification Alternatives & Compiler-Side Awareness

**Folder:** `curriculum/11-verification-alternatives-compiler-awareness/`

**Rationale:** Houses two toolchain items that this project deliberately scopes as single, non-default exceptions rather than ongoing tracks: cocotb (the Python-based verification alternative, appearing exactly once, never the default SystemVerilog-testbench flow) and TVM/MLIR (compiler-side awareness only, never a substitute for RTL work). Also directly serves the "collaborate with ML researchers" and "read a paper and translate it into hardware requirements" goals from the project's professional-profile definition, by exposing how a compiler maps a workload graph onto an accelerator's scheduling model.

**Example artifact:** reimplement Module 9's int8 requantization testbench in cocotb instead of SystemVerilog (the single demonstrative Python-verification example), plus a short compiler-side exercise mapping a small MLIR/TVM graph fragment onto Module 10's scheduler/controller — awareness only, no full compiler and no instruction-set architecture is built anywhere in this curriculum.

**Prerequisite:** Module 9 (needs an existing verified block to reimplement verification for), Module 10 (scheduler/controller the compiler exercise maps onto). Primer needed: cocotb basics, MLIR/TVM intermediate-representation concept at one paragraph.

---

## Module 12: Capstone — Integrated Accelerator Subsystem

**Folder:** `curriculum/12-capstone-integrated-accelerator-subsystem/`

**Rationale:** The portfolio-consolidation module for the final phase of the plan, and the top of the escalating-ambition model: a substantial multi-block subsystem rather than another single functional unit. Integrates the systolic array (Module 2), memory hierarchy and interconnect (Module 6), sparsity/MoE routing (Module 7), KV-cache management (Module 8), quantization (Module 9), and the scheduler (Module 10) toward the portfolio-level "interview-ready" readiness check defined in the project's evaluation-metrics framework.

**Bounded scope, to prevent this module from becoming an open-ended tail risk:** the REQUIRED minimum integration is the three most load-bearing subsystems only — systolic array (Module 2) plus scratchpad/memory controller (Module 6) plus scheduler (Module 10) — wired end-to-end and verified on one representative workload tile. Quantized-datapath integration (Module 9), sparsity/MoE routing integration (Module 7), and KV-cache integration (Module 8) are an explicit STRETCH extension, attempted only if the module's remaining time budget allows, and are not required for this module to count as complete. The project's existing month-18 interview-ready remediation loop remains the outer safety net if even the bounded minimum is not reached in time; this bounded scope addresses the capstone's own inner risk, it does not remove or replace that outer mechanism.

**Example artifact:** required minimum — systolic array plus scratchpad/memory controller plus tile scheduler, simulated end-to-end on one representative workload tile, with a combined throughput-and-area target checked in the same simulation/synthesis run. Stretch — extend the same integration to include the quantized datapath, sparsity/MoE routing, and KV-cache management, budget permitting. Either way, closes with a self-assessed whiteboard walkthrough of the design per the project's evaluation-metrics portfolio check.

**Prerequisite:** Module 2 (systolic array), Module 6 (memory hierarchy/interconnect), Module 7 (sparsity/MoE), Module 8 (KV-cache), Module 9 (quantization), Module 10 (scheduler) — six modules, matching the integration scope in the rationale above exactly. Primer needed: system-level integration and verification basics (interface contracts between previously-standalone blocks).

---

## Explicitly deferred to thin-awareness only (no dedicated module)

Per the project's continuous-validation approach and its technology radar, the following stay at brief-mention/quarterly-scan depth only — tracked, never built as a project. These items live in `curriculum/emerging_topics/` as brief, quarterly-updated awareness notes, not as full numbered modules with dedicated hardware artifacts; this is what currently populates that subfolder.

- Photonic computing
- Analog AI
- Neuromorphic computing
- Quantum ML
- State Space Models / Mamba / RWKV / RetNet — linear-time attention alternatives; candidates for promotion to a dedicated module if a future scope re-check shows they have stabilized across multiple hardware generations
- Liquid Neural Networks
- Diffusion-model-specific hardware demands beyond what Modules 2-10's general tensor/memory/scheduling patterns already cover
- World Models, Agentic AI, and test-time-compute scaling as hardware design targets in their own right (covered narratively in Section 0; not yet stable enough for a dedicated hardware-artifact module)
- Reasoning-model-specific extended test-time-compute scheduling demands

Promotion out of this list requires the same fundamental-vs-fad rubric every other module already passed, applied at the next quarterly checkpoint — not an ad hoc addition.
