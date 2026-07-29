# Module 0: Historical Context

Before I touch a single accelerator topic, I want to walk through how we got here. This module isn't nostalgia. It's the reasoning behind why AI hardware today looks the way it does, and why some "obviously correct" hardware bets failed while others, built on the same underlying idea, succeeded a decade later. I'll come back to that pattern more than once as we move through the eras below.

I'm using three primary dimensions to measure hardware design across this history: Power, Performance, and Area. These three aren't independent choices: they're the core trade-offs of digital electronics, the "golden triangle" that every hardware designer navigates. Raising performance or shrinking area almost always costs more power. Lowering power almost always means accepting slower performance or using more chip area. This triangle isn't a single named theorem with one founder, but it emerged as the industry standard through decades of engineering practice. The closest academic foundation is Clark D. Thompson's formalization of the area-time trade-off for VLSI circuits in the late 1970s [@thompson1979], which proved mathematical limits on simultaneous improvements in speed and area. For decades, this trade-off was softened by Dennard scaling, the pattern IBM researcher Robert Dennard described in 1974 [@dennard1974]: as transistor size shrank, voltage and current scaled proportionally, keeping power density constant. In other words, designers could improve performance and shrink area together while the power cost stayed hidden. That stopped working around 2005-2007, once leakage current and threshold voltage stopped scaling with transistor size, and power joined area and performance as an explicit, irreducible constraint [@esmaeilzadeh2011]. From that era onward, every choice appears in the PPA triangle. I'll use this lens across the eight eras below.

## Era 0: Computational Origins (pre-1950)

I'm starting this narrative on ENIAC (Electronic Numerical Integrator and Computer), not on Turing's 1936 computability work. That's a deliberate choice, so let me explain it before going further.

Turing's 1936 paper defines what's computable at all, via the Universal Turing Machine, and it's genuinely foundational [@turing1936]. But it has no hardware artifact. It's a theory-of-computation result, not a machine you can point to. ENIAC, on the other hand, is a specific machine, dedicated on a specific date, built from specific components. I can immediately measure it through the PPA framework: that's the point of this module.

ENIAC was unveiled on 14 February 1946 at the University of Pennsylvania, under a US Army wartime contract. It was the first large-scale, general-purpose, programmable electronic digital computer, built from around 18,000 vacuum tubes rather than mechanical relays, which is what let it run at genuinely electronic speed instead of being bottlenecked by moving parts. Multiple independent institutional sources describe it as the start of the electronic computer age, not just "a milestone" [@ethw1946] [@ieeespectrum2026] [@penntoday2021].

Plotted as the first historical point on the PPA graph, ENIAC dominates the area and power axes for all the wrong reasons: it sits at the extreme end of both, while its performance per watt is negligible. The machine occupied roughly 170 square meters and drew 150 kilowatts, yet performed around 5,000 floating-point operations per second. That tradeoff, enormous footprint and power for tiny computational throughput, is the defining point: ENIAC proved electronic computation was possible, but the architecture itself was brutally inefficient. The stored-program concept from EDVAC (Electronic Discrete Variable Automatic Computer), ENIAC's successor, showed how to escape this trap: by making machines programmable without rewiring, the next generation could reuse the same physical footprint and power budget to run different algorithms, improving the area-to-performance and power-to-performance ratios.

There's a sequencing quirk worth flagging here. Von Neumann's "First Draft of a Report on the EDVAC" was distributed in June 1945, roughly eight months before ENIAC's public dedication, and it contains the first published description of the stored-program architecture that bears his name [@vonneumann1945]. That looks backwards at first: the architecture concept predates the machine that inspired it. It isn't really backwards, though. Von Neumann had joined the ENIAC team by around September 1944, after learning of the project that August, so his report captures the conceptual leap that came out of working on ENIAC, published before ENIAC itself was unveiled to the public. I'm treating 1945-46 as one compressed origin beat rather than forcing strict date order onto it: ENIAC proved a general-purpose electronic machine could be built at all, and the EDVAC report described how to make the next one programmable without rewiring it by hand.

One more entry belongs in this era, and it predates both of the above. McCulloch and Pitts published "A Logical Calculus of the Ideas Immanent in Nervous Activity" in 1943, the first mathematical model of an artificial neuron [@mcculloch1943]. Their move was to formalise neuron firing as propositional logic: given a handful of physical assumptions, a neuron fires or doesn't (all-or-none, no in-between), a neuron fires when enough of its synapses are excited within a fixed time window regardless of what happened before, the only meaningful delay is the synapse itself, treated as one discrete time step, and a single active inhibitory synapse blocks firing outright. Under those assumptions, whether a neuron fires at a given time step can be written as a logical proposition, and its dependence on the neurons feeding into it becomes a logical implication built from AND, OR and NOT, exactly which one falls out of how its excitatory and inhibitory synapses are wired and how high its firing threshold is. That's the paper's real result: excitatory and inhibitory wiring doesn't just resemble boolean logic, it directly instantiates it, so any expression in propositional logic can in principle be built out of a net of these idealised neurons. It has no hardware behind it at all, it's pure logic and mathematics, but it's the conceptual seed that every neural-network hardware story in this curriculum eventually traces back to. It's worth sitting with the fact that this idea existed three years before ENIAC was switched on.

The last beat of this era is a component-level story rather than a machine-level one. Bardeen and Brattain first amplified a signal with a point-contact semiconductor device on 16 December 1947 at Bell Labs, with the public announcement following on 30 June 1948 [@computerhistory1947] [@ieeeusa2022]. The transistor drew little contemporary attention at the time, which is easy to miss in hindsight given it's the physical substrate that eventually replaces the vacuum tube entirely, and underwrites every Moore's-Law-era scaling story that follows it. I'm placing it here, right after ENIAC, because that's the order these things actually happened: general-purpose electronic computation existed first, running on vacuum tubes, and only afterwards did the component that would eventually replace them get invented.

## Era 1: Symbolic Founding, First Hype (1950s-60s)

Turing published "Computing Machinery and Intelligence" in 1950. He sidesteps the question "can machines think?" as too loaded to answer directly, and replaces it with the Imitation Game: can a machine's conversation be mistaken for a human's [@turing1950]. It's a philosophical paper, not a hardware one, but it's the first time the question of machine intelligence gets asked in a form precise enough to be tested, and the Turing Test still shapes how "AI progress" gets framed in the press today. Six years later, the field would get a name and a research identity of its own.

The Dartmouth Conference, held over the summer of 1956, is where "artificial intelligence" gets named as a distinct field, organised by McCarthy, Minsky, Rochester, and Shannon [@dartmouth1956]. Before this, what we're calling AI was just part of "computing" generally. After it, AI has a name, a research identity, and eventually its own funding cycles, which matters for the eras that follow this one.

Two years after Dartmouth, in 1958, Rosenblatt published the Perceptron, the first trainable neural network model with an actual learning algorithm [@rosenblatt1958]. What I want to draw attention to here is that this wasn't just an algorithm on paper. The same year, the Mark I Perceptron was built as a physical machine at Cornell Aeronautical Laboratory: a 20x20 grid of photocells acted as its "retina," feeding 400 inputs into a layer of randomly-wired association units, whose weights were stored and adjusted using motorised potentiometers. Trained on simple geometric shapes, it could learn to tell them apart after a handful of examples [@rosenblatt1958hw]. That's worth pausing on: the first hardware built specifically for a neural network is fifteen years older than most people would guess, and it's analog, electromechanical, and nothing like the digital accelerators the rest of this curriculum focuses on. It's still the direct ancestor of the whole lineage.

The Mark I Perceptron is also where this module's recurring hype pattern first shows up. On 8 July 1958, the New York Times ran "NEW NAVY DEVICE LEARNS BY DOING", after a Navy-organised press conference, speculating that the machine would eventually "walk, talk, see, write, reproduce itself and be conscious of its existence" [@nytimes1958]. This is the first documented AI hype and expectation-gap cycle I'll be pointing back to later in this module, when the same shape of overpromise-then-funding-cut repeats in Era 2 and again in Era 3. It's worth being honest that the coverage itself is well documented, but the direct causal link between this specific press cycle and the AI winter that eventually followed is more of an interpretive claim than a settled fact.

Not every strand of the field's early years ran through hardware, though. The dominant paradigm through the 1950s and 60s was symbolic AI, often called GOFAI (Good Old-Fashioned AI): intelligence built from hand-coded rules and logical inference over symbols, rather than learned from data. Newell, Shaw and Simon's General Problem Solver, reported in 1957 and published in 1959, is the concrete anchor for this: a single program meant to solve any problem expressible as a set of formal rules and a goal state, using means-ends analysis to close the gap between the two [@newell1959]. Learning-based approaches weren't absent, though. That same year, Arthur Samuel coined the term "machine learning" itself, in a paper describing a checkers-playing program that improved by playing against itself [@samuel1959]. The two approaches, rule-based and learning-based, coexisted from the field's earliest years; it's only in hindsight that one looks like the default and the other the exception.

Joseph Weizenbaum built ELIZA in 1966, the first chatbot, using simple pattern matching and scripted substitution to simulate a Rogerian psychotherapist [@weizenbaum1966]. The name isn't an acronym: it's a nod to Eliza Doolittle from George Bernard Shaw's *Pygmalion*, a character trained to sound refined despite her humble origins, mirroring how the program turned rigid, mechanical input into natural-sounding conversation. There's no understanding behind it at all, just string matching against a script, but Weizenbaum was unsettled by how readily his own secretary and other users attributed real understanding and empathy to it, some asking to be left alone with the program. That reaction is what later got named the "Eliza effect": the tendency to read genuine comprehension into a system that's mechanically simple, once it produces the right surface behaviour. It's a pattern that resurfaces every time a new generation of language systems gets mistaken for something more than it is.

There's a more direct, technical cause for the funding collapse that Era 2's bullets describe, and it belongs here rather than there. Minsky and Papert published *Perceptrons* in 1969, a rigorous mathematical treatment of what the Perceptron architecture could and couldn't compute, and it showed that a single-layer Perceptron can't solve XOR, a genuinely basic case of a not-linearly-separable problem [@minskypapert1969]. That's not a funding story or a press cycle, it's a proof, and it lands squarely on the hardware Rosenblatt had built and championed. The NYT hype cycle above set unrealistic public expectations; this book gave researchers and funders a rigorous technical reason to stop believing the specific architecture could deliver on them. Both strands feed into Era 2.

## Era 2: First AI Winter (1970s) - ONGOING

- Lighthill Report, UK, 1973: concluded AI had failed to meet its ambitious goals, triggering sharp UK funding cuts.
- Mansfield Amendment, US Congress, 1973: barred ARPA from funding non-military-relevant research, cutting roughly $3M/year from CMU speech research.
- Dendral (Stanford, from 1965) and MYCIN (Stanford, 1972): early expert systems for chemical analysis and medical diagnosis, the concrete symbolic-AI technology this era's funding cuts were reacting to.
- Historiographical dispute to present without resolving: mainstream sources describe a clear 1973-1980 funding collapse, while a dissenting source argues the "first AI winter" label oversimplifies the record.
- No fixed milestone paper covers this era; it's a documented gap, not an oversight.

## Era 3: State Bets & Second AI Winter (1979-93) - ONGOING

- Fixed papers: Kung & Leiserson systolic arrays, Mead neuromorphic computing, Rumelhart/Hinton/Williams backpropagation.
- Japan's Fifth Generation Computer Systems Project, launched 1982, ~$400M MITI-backed bet on specialised parallel hardware, failed commercially by the early 1990s against general-purpose commodity machines.
- Collapse of the Lisp-machine market, 1987, Symbolics bankruptcy 1993: specialised AI hardware losing outright to general-purpose workstations.
- Narrative role: a direct cautionary counterpoint to Era 5, prefiguring the Hardware Lottery theme (Hooker 2021).

## Era 4: Preconditions for Deep Learning (1997-2009) - ONGOING

- Fixed papers: LeCun LeNet, Hochreiter/Schmidhuber LSTM.
- Deep Blue defeats Kasparov, May 1997: first mass "AI beats humanity's best" demo.
- Naive Bayes spam filters (mid-1990s) and Amazon's item-to-item collaborative filtering (patented 1998, deployed early 2000s): machine learning's shift from research demos to everyday consumer infrastructure, years before the deep learning boom.
- Dennard scaling breakdown, ~2005-2007: the physics-level reason general-purpose clock scaling stopped being free, forcing the shift to multi-core then specialised silicon.
- AWS EC2 launch, 2006, and NVIDIA CUDA (2006) / Tesla line (2007): cloud delivery and GPUs beginning their pivot to general-purpose compute.
- ImageNet dataset published, 2009: the data precondition for Era 5.
- Hinton, LeCun and Bengio's early-2000s deep learning revival work, later recognised with the 2018 ACM A.M. Turing Award: the sustained research effort behind this era's LeNet and LSTM papers.

## Era 5: Deep Learning + GPU Era (2012-17) - ONGOING

- Fixed papers: Krizhevsky AlexNet, Dean DistBelief, Goodfellow GANs, Silver AlphaGo, Jouppi TPU, Vaswani Transformer.
- IBM Watson wins Jeopardy!, 2011: mass-media NLP milestone preceding the GPU-driven trajectory.
- Google's neural machine translation system launched, November 2016: a sudden, widely noticed jump in translation quality, one of the first times deep learning's improvement was obvious to ordinary consumers rather than only benchmark-watchers.
- AlphaGo defeats Lee Sedol, March 2016: deep learning plus RL plus TPU-scale compute achieving a milestone experts thought was a decade away. Game 2's "Move 37" became the emblematic moment, a move no human professional would have played, that commentators and Lee Sedol himself initially read as a mistake.
- Narrative role: specialised AI hardware (TPUs) reappears and succeeds here, where Era 3's specialised hardware failed.

## Era 6: Scale, Access, Mass Awareness (2017-22) - ONGOING

- Fixed papers: Vaswani Transformer (carried over from Era 5), Hooker Hardware Lottery.
- OpenAI founded, December 2015; GPT-1 published, June 2018; GPT-2 released with staged rollout, February 2019 over concerns about misuse: the lineage that led directly to GPT-3 below.
- GPT-3 API released, June 2020: the model-as-a-service business model.
- Stable Diffusion released, August 2022: open-weights, consumer-GPU-capable, contrasted with DALL-E 2/Imagen's closed cluster-only access.
- ChatGPT public release, November 2022: fastest consumer application growth in internet history, the "no single defining paper, but a defining moment" case.

## Era 7: Present Frontier (2022-now) - ONGOING

- No fixed milestone paper anchors this era, by design.
- Post-ChatGPT competitive scramble, 2023: Google, despite having invented the Transformer, was reportedly caught off guard and declared internal "code red"; Microsoft, Amazon, Meta, and Musk's newly founded xAI all entered the race within the year.
- OpenAI o1, preview September 2024, full release December 2024: the first mainstream reasoning model using test-time (inference-time) compute as a distinct scaling axis from training-time compute.

## References

- **[@computerhistory1947]** Computer History Museum (n.d.). *1947: Invention of the Point-Contact Transistor*. https://www.computerhistory.org/siliconengine/invention-of-the-point-contact-transistor/
- **[@dartmouth1956]** Dartmouth Alumni Magazine (n.d.). *The Birth of Artificial Intelligence*. https://dartmouthalumnimagazine.com/articles/birth-artificial-intelligence
- **[@dennard1974]** Dennard, R. H., Gaensslen, F. H., Yu, H.-N., Rideout, V. L., Bassous, E. and LeBlanc, A. R. (1974). *Design of Ion-Implanted MOSFET's with Very Small Physical Dimensions*. IEEE Journal of Solid-State Circuits, 9(5), 256-268. https://doi.org/10.1109/jssc.1974.1050511
- **[@esmaeilzadeh2011]** Esmaeilzadeh, H., Blem, E., St. Amant, R., Sankaralingam, K. and Burger, D. (2011). *Dark Silicon and the End of Multicore Scaling*. https://doi.org/10.1145/2000064.2000108
- **[@ethw1946]** ETHW Milestones (n.d.). *ENIAC, 1946*. https://ethw.org/Milestones:Electronic_Numerical_Integrator_and_Computer,_1946
- **[@ieeespectrum2026]** IEEE Spectrum (2026). *ENIAC, the First General-Purpose Digital Computer, Turns 80*. https://spectrum.ieee.org/eniac-80-ieee-milestone
- **[@ieeeusa2022]** IEEE-USA InSight (2022, May 16). *Bell Labs and the Transistor*. https://insight.ieeeusa.org/articles/your-engineering-heritage-bell-labs-and-the-transistor/
- **[@mcculloch1943]** McCulloch, W. S. and Pitts, W. (1943). *A Logical Calculus of the Ideas Immanent in Nervous Activity*. https://doi.org/10.1007/BF02478259
- **[@minskypapert1969]** Minsky, M. and Papert, S. (1969). *Perceptrons: An Introduction to Computational Geometry*. MIT Press.
- **[@newell1959]** Newell, A., Shaw, J. C. and Simon, H. A. (1959). *Report on a General Problem-Solving Program*. Proceedings of the International Conference on Information Processing, pp. 256-264, Paris: UNESCO House.
- **[@nytimes1958]** The New York Times (1958, Jul 8). *New Navy Device Learns By Doing*. https://www.nytimes.com/1958/07/08/archives/new-navy-device-learns-by-doing-psychologist-shows-embryo-of.html
- **[@penntoday2021]** Penn Today (2021). *The world's first general-purpose computer turns 75*. https://penntoday.upenn.edu/news/worlds-first-general-purpose-computer-turns-75
- **[@rosenblatt1958]** Rosenblatt, F. (1958). *The Perceptron*. https://doi.org/10.1037/h0042519
- **[@rosenblatt1958hw]** Rosenblatt, F. (1958). *Mark I Perceptron* (hardware, Cornell Aeronautical Laboratory). Smithsonian National Museum of American History, *Electronic Neural Network, Mark I Perceptron*. https://americanhistory.si.edu/collections/object/nmah_334414
- **[@samuel1959]** Samuel, A. L. (1959). *Some Studies in Machine Learning Using the Game of Checkers*. IBM Journal of Research and Development, 3(3), 210-229. https://dl.acm.org/doi/10.1147/rd.33.0210
- **[@thompson1979]** Thompson, C. D. (1979). *Area-Time Complexity for VLSI*. https://doi.org/10.1145/800135.804401
- **[@turing1936]** Turing, A. M. (1936). *On Computable Numbers, with an Application to the Entscheidungsproblem*. https://doi.org/10.1112/plms/s2-42.1.230
- **[@turing1950]** Turing, A. M. (1950). *Computing Machinery and Intelligence*. https://doi.org/10.1093/mind/LIX.236.433
- **[@vonneumann1945]** Von Neumann, J. (1945). *First Draft of a Report on the EDVAC*. https://archive.org/details/vnedvac
- **[@weizenbaum1966]** Weizenbaum, J. (1966). *ELIZA: A Computer Program for the Study of Natural Language Communication Between Man and Machine*. https://dl.acm.org/doi/10.1145/365153.365168
