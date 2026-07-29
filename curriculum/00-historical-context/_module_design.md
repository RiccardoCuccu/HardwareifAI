# Module 0: Historical Context

## Why this module exists

Every technical module in this curriculum starts from a hardware artifact and works backwards to the principle it demonstrates. Before any of that, I want the reader to have a map of how we got here at all: why AI hardware looks the way it does today, and why some of yesterday's "obviously correct" hardware bets failed anyway.

This module exists to set that frame. It's the one place in the curriculum where I zoom out to the full arc, from the first stored-program machines to the present frontier, and trace it through the same five-dimension lens (compute, memory, bandwidth, parallelism, communication) that every later module applies to a narrower slice. The First Principles doctrine (Manifesto Principle 2: study the underlying fundamental, not the brand name) only makes sense once you've seen it play out historically, more than once, across completely different hardware generations. Specialised AI hardware has both spectacularly failed (Era 3) and spectacularly succeeded (Era 5) at different points, for reasons that have very little to do with the quality of the underlying idea and a lot to do with what the general-purpose hardware landscape looked like at the time. That's the Hardware Lottery thesis (Hooker, 2021, already on the fixed paper list), and this module is where I show it happening in real time, across eight eras, before the rest of the curriculum ever mentions it by name.

## Scientific foundation

This module cites the earliest entries from the curriculum's fixed milestone-paper list: see `papers/seminal_papers.md` for full citations and context on von Neumann (1945), Turing (1950), McCulloch & Pitts (1943), and Rosenblatt's Perceptron and Mark I Perceptron (both 1958). For the non-paper historical and industry events this module also draws on (ENIAC, the transistor, the Dartmouth Conference, and later), see this file's own `## References` section in `00-historical-context.md`.

## Hardware implications

Each era in this module's body applies the five-dimension lens explicitly: compute, memory, bandwidth, parallelism, communication. The point isn't just to list dates, it's to show how each transition actually changed those five things, since that's the same lens every later module in the curriculum uses on a narrower topic.

## Prerequisites

None. This is the first module.

## Projects

This module has no associated hardware-artifact project. It is a deliberate, documented exception to the curriculum's usual rule that every module pairs with a hardware artifact (see the project's Manifesto Principle 4): Module 0 is the context-setting module that precedes any toolchain onboarding, so there is nothing yet to build against.
