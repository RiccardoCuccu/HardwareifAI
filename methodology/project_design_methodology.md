# Project Design Methodology

*Describes how hands-on hardware projects are designed for each module.*

## Why every topic needs a project

This is the real added value of the whole curriculum. Every concept has to have a project that proves it was actually understood, not just read about. Given the target sub-role (AI-accelerator RTL/microarchitecture design, not ML tinkering, per [`vision/target_audience.md`](../vision/target_audience.md)), a project only counts toward the curriculum's goal if it produces a concrete hardware artifact. An ML-only or software-only exercise, such as fine-tuning a model or writing a training loop with no hardware component, does not count, however educational, because it does not prove RTL/microarchitecture competence. This is principle 4 of [`vision/manifesto.md`](../vision/manifesto.md): implementation over memorisation.

For every topic on the dependency graph (see [`dependency_graph_methodology.md`](dependency_graph_methodology.md)), the design question is: "what is the smallest hardware artifact that proves this competence was acquired?"

## The hardware-artifact definition

Every module project must produce all of:

1. **RTL** implementing the concept the module covers.
2. **A testbench and simulation**, using an open-source, free toolchain only, never a paid EDA tool. The specific toolchain used across the curriculum is defined separately, not restated here.
3. **FPGA deployment where feasible**, on free/open toolchains, as an optional extension rather than a requirement.
4. **A stated, measured power/performance/area/throughput target**, defined before the work starts and checked against the simulated or synthesised result at the end. Power is a required target here, stated and checked like the other three; the project is free to use whatever technique is appropriate to hit it, nothing is ruled out in advance. This is what satisfies the functional-test-plus-target evaluation criterion below.

## Escalating ambition

Projects follow the same escalation model described at the philosophy level in [`vision/learning_philosophy.md`](../vision/learning_philosophy.md): early-curriculum projects are small, single-purpose hardware units (one functional block, verified standalone); later projects compound into substantial multi-block subsystems as skill and portfolio depth grow. This page defines what "small" and "substantial" concretely look like for a project design, not just the principle behind the escalation.

Worked example, usable as the template for new projects: a small systolic-array multiply-accumulate (MAC) array, sized e.g. 4x4 int8 MACs.

- **Functional test**: a testbench and simulation, feeding known input matrices and checking output against a golden reference, covering at minimum reset behaviour, pipeline fill/drain, and back-to-back streaming inputs.
- **Power/performance/area target, stated up front**: sustained throughput of one MAC-array-output per clock cycle once the pipeline is full, an estimated or simulated power/energy figure, and a cell/area count kept under an explicitly stated budget for the target process assumption.
- **Pass criteria**: the testbench passes with zero mismatches against the golden reference, the synthesis report meets the stated area and power budgets, and the simulated waveform confirms the expected pipeline latency.

A smaller-scope, earlier-curriculum variant of the same idea: a single quantisation unit (e.g. an int8 requantisation block with configurable scale/zero-point), verified the same way, as the escalation on-ramp before attempting the full MAC array.

## Evaluation: functional test plus target, not test pass alone

A project is complete when it passes its own defined functional test suite (simulation-verified correctness) AND hits its stated power, performance, area, or throughput target defined at design time. Passing tests with no target met does not count as complete: this is what distinguishes "it works" from "it works well enough to matter for the target role." This criterion is fully self-verifiable: the simulator and synthesis tool produce the pass/fail result directly, with no external party needed. Where a module is grounded in a specific paper's published result (see [`paper_selection_criteria.md`](paper_selection_criteria.md)), reproducing that published benchmark or figure is additional, equally self-verifiable evidence that the underlying concept was actually understood.

## Recording the project's rationale

Every project is documented using [`templates/project_template.md`](../templates/project_template.md), and every topic it demonstrates gets a Decision Log identity card recording which project proves the competence, per [`templates/decision_log.md`](../templates/decision_log.md). A module's own `module_design.md` (per [`templates/module_template.md`](../templates/module_template.md)) links its Projects section back to the concrete artifact under `projects/`.

## Open items

This page grounds the hardware-artifact definition, the escalation model, and the functional-test-plus-target criterion, all directly sourced from the project's existing design reasoning. It does not yet define a fixed set of power/area/process assumptions to use as defaults across projects (the worked example above states its own budget ad hoc); a shared default process/library assumption may be worth fixing once the first two or three real projects have been built and their actual synthesis constraints are known.
