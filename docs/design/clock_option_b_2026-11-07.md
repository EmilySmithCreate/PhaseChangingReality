# Option B: a clock on every point, tied to the lengths of its links (7 November 2026; her "proceed")

*Her decision of 7 November 2026 (the notebook, verbatim): "Option B is a rule that ties each point's tick to the
lengths of its links, so that clocks run slow where links are long, near mass. This is a good idea proceed." Built
the same day in its plainest form, ours, as `graphity.clock`, with tests (`tests/test_clock_option_b.py`) and one
sandbox look (`sandbox/clock_option_b_look.py`, LOG). Nothing registered: the first registered test on it needs her
prediction (below).*

## Current definitions (from `HYPOTHESIS.md`, Gravity; unchanged here)

- The carrier of gravity is the edge lengths: a length on every link, 1 + delta, relaxed at no cost from the curl
  with one constant alpha, negative, so links are longer near a knot; the total length is fixed (her scale rule);
  gravity acts in two and three dimensions, light only in three; the stiffness of the lengths is exact (4 times
  the lattice Laplacian per axis family, six-link and four-link forms).
- The toy's own clock, the count of accepted moves per point, is a clock of activity, not of proper time: it runs
  faster near a knot (T101, T101 Amendment 1).
- **New (7 November): a point's tick rate is the inverse of the mean length of its 2D links** (four on the sheet,
  six in the cube). Proper ticks at a point after t global ticks are t times its rate.

## What the rule puts in by hand, and what it does not

- **Put in: the sign.** Clocks run slow near mass because alpha is negative. With alpha positive they would run
  fast (a test holds both). The sign was decided on 4 November for light's delay; the clock inherits it. This is why
  option B waited on her word: the time half of gravity is not derived here, it is tied to the space half.
- **Put in: equal parts at first order.** In Einstein's account the delay of light past a mass has two equal
  sources at first order, the longer path and the slow clocks (general knowledge, to verify: the Shapiro delay
  in the parametrised post-Newtonian form is proportional to 1 + gamma, gamma = 1 in general relativity, one part
  from the time and one from the space). Under option B both parts come from one field, delta, with the same
  weight, so a photon spending one *local* tick per unit of length is delayed by (1 + delta) squared, about
  1 + 2 delta: the two halves are equal by construction, not by measurement. A test of "equal parts" would test
  nothing. What can be tested is below.
- **Not put in: the balance.** Exact, from her scale rule: the mean over all points of the mean link length is 1,
  so the mean of 1 over the tick rate is exactly 1 on every sheet and cube (a test holds it to 1e-12). Clocks
  slow near a knot are balanced by clocks a shade fast far from it. On a torus there is no infinity to set a
  clock against, only the mean; in the sky the far clock is the standard, and the toy's far clocks run fast by
  the knot's share of the total length. Convention, not a measurement: a different scale rule would move the
  zero.
- **Not put in: the shape of the slowing with distance.** It is the lattice Green's function of the stiffness, the
  same field that lengthens the links. In the continuum this is the logarithm on a sheet and 1 / r in a cube,
  the Newtonian potential's shape (general knowledge, to verify), so option B says the clock's slowing has the
  shape of the potential, which is what the measured time dilation on Earth has at first order (the Pound and
  Rebka and the GPS corrections, general knowledge, to verify). On the toy's finite tori the look reads a faster
  fall-off than 1 / r (below): the periodic images and the mean subtraction bend it. The registered form of this
  claim is hers to predict.

## The look of 7 November (sandbox, not a test; `sandbox/out/clock_option_b_look_2026-11-07.txt`)

One planted switch, alpha = −0.5 (the tests' value; T84's landscape covered a range of alpha). Sheet 32 × 32, the
four-link lengths: the slowing 1 − rate reads 0.15 at distance 1 from the knot, 0.09 at 3, 0.04 at 6, 0.008 at
9, crossing zero at 10 and settling at −0.05 (fast) at the far side; the ratio of one band's slowing to the
previous falls from 0.84 to 0.45 as the zero approaches. Cube 12³, the six-link lengths: 0.039 at the knot, 0.018
at 1, 0.009 at 2, 0.0045 at 3, 0.0015 at 4, then fast by 0.006 at the far side; each band about half the one
before over the first three steps, faster than 1 / r (which would give two thirds, then three quarters). The mean
of 1 over the rate is 1.000000000000 on both, as the exact statement says.

## What is owed before a registered test (hers)

Her prediction, in her words, for **the shape of the clock's slowing with distance from one knot in the cube**: the
fitting sizes and a held-out size; a number or a range for the ratio of the slowing at distance 2 to the slowing
at distance 1 at the held-out size (the look reads 0.50 at 12³ with the knot's images in play). Candidate forms,
ours: (a) 1 / r, the Newtonian shape, ratio one half at 2 against 1; (b) the lattice Green's function on the finite
torus, computed exactly before the run, which is what the code does and so is a check of the build, not of the
hypothesis; (c) her own form. Only (a) or (c) can fail.

## Record

`HYPOTHESIS.md` (Gravity, Time; her decisions of 7 November); `STATE.md` (piece 10; owed item 4 closed);
`docs/OWED.md` item 4; `TOY.md` code map; the notebook, 7 November; `sandbox/LOG.md`.
