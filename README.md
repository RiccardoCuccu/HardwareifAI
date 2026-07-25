# HardwareifAI

An open-source curriculum for hardware engineers who want to design the chips that run AI, not just read about them.

> **Status:** early and pre-alpha. This repository was just created and is actively being built out. Most folders below are scaffolding right now, not finished content. Expect the structure to fill in incrementally over the coming months rather than all at once.

## What this is

HardwareifAI is a hardware-first curriculum for AI-accelerator design: the memory hierarchies, compute patterns, parallelism models, and communication trade-offs that decide whether a chip can actually run modern AI training and inference well.

It's built for people who already think like hardware engineers (RTL, microarchitecture, digital design) and want a structured, engineering-driven path into the AI-accelerator space, not a crash course in machine learning theory.

Two things make it different from a typical study plan:

- **Every topic is paired with a real hardware artifact.** SystemVerilog RTL, verified in simulation with a free and open-source toolchain, not slides or a written summary. If a topic doesn't produce something you can simulate, it isn't done.
- **First principles over frameworks.** Named technologies (FlashAttention, CUDA, a specific GPU) are treated as case studies of an underlying fundamental (memory-traffic minimisation, the parallel programming model, massively parallel architectures), never as the subject itself. The goal is a curriculum that stays useful after the current paradigm is replaced, not one tied to this year's hype cycle.

## Who it's for

Hardware and digital-design engineers moving into AI-accelerator design, not ML software engineers picking up hardware as a side interest. If your background is SystemVerilog, RTL, and verification and you want a serious, problem-first path into designing the hardware behind AI training and inference, this is built for you.

## Core philosophy

This isn't "one person's study plan." It's a collaborative, transparent, and reproducible curriculum: not just the content, but the reasoning behind why it contains these topics and not others. The full decision process (how topics get selected, ordered, validated, and eventually retired) is published alongside the curriculum itself, in [`vision/manifesto.md`](vision/manifesto.md). That transparency is a core deliverable of this project, not an afterthought.

## How the repository is organised

```
vision/         why this project exists, who it's for, the guiding philosophy
methodology/    how the curriculum itself gets designed: topic selection, paper criteria, validation
curriculum/     the actual modules, organised by category, each with an associated hardware project
taxonomy/       AI model taxonomy, hardware taxonomy, and the dependency graph tying it together
papers/         seminal and recent papers, reviewed against what they change for hardware
projects/       the hands-on SystemVerilog artifacts that prove each module was actually understood
resources/      books, courses, and other freely accessible supporting material
community/      contribution guidelines and how to get involved
```

Read [`vision/manifesto.md`](vision/manifesto.md) first if you want the "why" before the "what".

## How to get involved

Contributions are genuinely welcome and strictly optional. This project is designed to succeed on self-directed work alone, so don't feel obligated to jump in, but if you'd like to:

- Open an [issue](../../issues) to propose a topic, flag a gap, or discuss a design decision.
- Use [Discussions](../../discussions) for anything more open-ended.
- Watch the repository if you'd rather follow along than participate directly.

There's no fixed contribution cadence and no expectation of ongoing involvement. Drop in whenever something catches your interest.

## License

Released under the [MIT License](LICENSE).
