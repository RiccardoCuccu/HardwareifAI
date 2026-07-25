# Manifesto

## Why this exists

There's no shortage of material for people learning AI from the software side. Courses, tutorials, and blog posts on machine learning, deep learning, and LLMs are everywhere. What's genuinely thin on the ground is a structured path for people coming from the other direction: hardware and computer architecture, who want to understand how to design the chips that actually run this stuff.

This project fills that gap. It's built by a digital-design engineer transitioning into AI-accelerator hardware, starting from the vantage point of someone who already thinks in RTL, microarchitecture, and verification, not someone learning both hardware and AI from scratch at the same time.

## The reframe

This isn't "one person's study plan that happens to be public." It's a collaborative, open-source curriculum for training AI-accelerator hardware engineers, built with a transparent and reproducible methodology.

That distinction matters. A study plan is optimised for one person's gaps and can afford to be idiosyncratic. A curriculum has to justify itself: why this topic and not that one, why this order, why this project as the proof of competence. Every design decision here is made the way the methodology below describes, not by gut feel, and the reasoning is written down so anyone can audit it.

The biggest risk with a self-made curriculum is mirroring how textbooks are ordered: machine learning first, then deep learning, then transformers, and so on. That ordering feels natural but isn't how companies actually hiring for AI-accelerator roles think. They reason from engineering problems outward, not from a syllabus. This curriculum is built the same way: problem-first, market-anchored, and revised against reality rather than against a fixed table of contents.

## The Curriculum Design Manifesto

Five principles govern every topic, module, and project decision made in this curriculum:

**1. Hardware first, software aware.** This isn't a course for training ML researchers. It trains hardware engineers who understand software well enough to design good hardware for it.

**2. First principles over frameworks.** Don't learn CUDA because CUDA exists. Learn the parallel programming model, with CUDA as one implementation example among others.

**3. Papers over tutorials.** Every important concept is traced back to the scientific literature that introduced or established it, not to a secondary summary of it.

**4. Implementation over memorisation.** Every module ships with an associated hardware project. Understanding a concept means being able to implement and verify it, not just describe it.

**5. Timeless knowledge over hype.** Every module explicitly separates fundamentals, consolidated technologies, and emerging research, so it stays honest about what's durable and what's still unproven.

## First principles, not brand names

For every candidate topic, the test is the same question: am I studying this because it's fundamental, or because it's popular right now?

The practical version of that test is a substitution: replace the trendy named thing with the underlying fundamental it's an instance of, and treat the named thing as a case study rather than the subject itself.

- Don't study FlashAttention because it's FlashAttention. Study memory-traffic minimisation; FlashAttention becomes a worked example of it.
- Don't study CUDA. Study the parallel programming model; CUDA becomes one implementation of it.
- Don't study the H100. Study massively parallel architectures; the H100 becomes an example of the class.

Applied consistently, this is what keeps the curriculum useful past the current hype cycle. When the next architecture supersedes transformers the way transformers superseded RNNs, the underlying fundamentals (memory movement, parallelism, compute patterns) are still exactly what a hardware designer needs to reason about.

## The methodology is public, on purpose

Most curricula publish the program (here's what we teach) but never the reasoning behind it (here's why this and not that). That gap is exactly where this project tries to be different.

The decision process for what enters the curriculum, in what order, and why, is published alongside the content itself, not kept as an internal working document. Every included topic is traceable to a written rationale: why it was included, what alternatives were considered and rejected, which competence it develops, and which hardware project demonstrates it. That transparency is treated as a first-class deliverable of this project, on equal footing with the curriculum content itself, not a nice-to-have.

The reasoning is what makes this reproducible by anyone else, not just usable by whoever happens to read the finished modules.

## An open invitation, not an obligation

This repository is public by default: the code, the commits, the design decisions, all of it. External engagement through issues, discussions, or elsewhere is genuinely welcome, but it's never required for the project to succeed. It's designed to work end to end on self-directed effort alone. If you find something useful here or want to weigh in, the door is open. If you don't, that's a perfectly fine outcome too.
