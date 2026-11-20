# The bag in the toy: what costs energy for the volume a third keeps open (20 November 2026, draft for her)

*Written on 20 November 2026 after her "read and proceed" on the bag model and her "I think both" on its two
candidate sources. Nothing here is a result. Nothing is built, fitted or registered until she has accepted or
changed each choice in section 6 (rule 20). The reading behind it is in
`docs/reading/notes/2026-11-20_hawking_page_and_the_wilson_line.md`; her words are in `sandbox/NOTEBOOK.md`.*

## 1. Current definitions (from `HYPOTHESIS.md`; unchanged here)

- **The count is energy, not length** (hers, 20 November). Mass has parts, each in its own unit (30 October).
- **Twist** lives only where there is curl: no curl, no twist. Matter's twist is in thirds on the box diagonals;
  only the box diagonals exist; the published charge table is a measuring tool (hers, 20 November).
- **The zero-total rule** (hers; softened to a steep price on straying): curl and uncurl total zero over one
  joined surface.
- **λ** (hers): open space sits at 1 or slightly below; above 1 only in a black hole's inner shell.
- **The toy's energy** (exact, six links, `TOY.md`): 16(3N − S) + 4λX = 4 · uncurl + 4(λ − 1) · curl. Curl on a
  link is a square above flat; uncurl a square below.
- **Light.** Hers: on the cube diagonals, in three dimensions only. The toy's built light (term 10) is the
  published lattice light on the links: a stand-in, labeled as such wherever it is used.
- **The proton** (hers, 20 November): a closed ring with a silent arc.

## 2. The published object to match

K. Johnson's 1975 lectures on the M.I.T. bag model: a particle's mass is the least value over its radius R of
(motion of the things held in, as 1/R) + B × volume − (a quantum term, as 1/R) + (a spin term, as 1/R). One
constant B, 57.5 MeV for every cubic fermi, is the cost of keeping the region open. At the best radius the volume
term is exactly a quarter of the mass. Reproduced to 0.6 % of his table (`sandbox/bag_look.py`). His own misses and
their published corrections are in the reading note.

## 3. The two candidate sources of that cost in her picture (her decision: both)

**(C) The uncurl partner.** A third must keep curl (no curl, no twist). Every unit of curl needs a unit of uncurl
(zero total). In the energy above, uncurl costs 4 a unit at every λ; curl alone costs 4(λ − 1). So under zero
total each unit of curl kept costs 4λ: 4 at λ = 1. *Exact so far:* the identity (`TOY.md`), checked by arithmetic
on two wirings of 20 November (the slab 4 × 6 × 6: 16(432 − 468) + 4λ · 144 = 4(λ − 1) · 144; the 4 × 4 × 6:
16(288 − 336) + 4λ · 192 = 4(λ − 1) · 192; both curl only). *Not known:* how much curl a third keeps; whether the
cost goes as the patch's points or as its edge.

**(D) Light's push.** A region that keeps light out pays for it. *Exact so far, with the stand-in light:* on the
curled tube, light adds 0.11 to 0.24 of its coupling to the free energy of every point, at every stiffness tried
(`sandbox/wilson_line_look.py`, Part 4). *Not known:* the same for a patch inside open space; the same for her
light, which is not built as a field.

## 4. The exact tests, cheapest first (named before anything is built)

1. **Read first:** T54's completed-patch energies (registered, read; O118) against the form
   b × (points in the patch) + s × (its edge). No new run.
2. **Reproduce:** the tube's 4(λ − 1) a point and the look's 0.11 to 0.24 a point, from the code as it stands.
3. **(C) on a patch:** a patch of curl with its matching uncurl in flat six-link space at λ = 1, at three sizes;
   the energy against points and edge. The largest size is predicted from the two smaller before it runs (rule 14).
4. **(D) on the same patches:** the free energy light adds, exact where the squares allow it, sampled otherwise
   with the tube as the check.

## 5. What would count, and what would not

- If the patch's cost goes as its points under (C), (D) or both, the toy has a cost for volume: a bag constant in
  toy units, and the ratio of the two sources. If it goes only as the edge, the toy has a surface cost and no bag.
- No constant is chosen to reach 57.5 MeV for every cubic fermi (rule 13). There is no map from toy units to MeV
  and fermi yet; without one nothing here is compared with a measurement.
- A look cannot crown either source (rule 16). A registered test follows only after her prediction is written.

## 6. Choices (defaults ours; hers to accept or change)

1. **How much curl a third keeps:** default one unit of curl for each third.
2. **Zero total on the patch:** default the hard form (curl = uncurl exactly inside the patch), since that is what
   makes (C) cost anything.
3. **Whose light for (D):** default the stand-in (term 10) first, labeled; her light as a field on the cube
   diagonals is a separate build with its own brief.
4. **The patch's shape:** default the smallest block of cells that holds one closed ring of three thirds.
5. **Her prediction, before test 3 runs:** points, edge, or both? (To be recorded in her words.)

## 7. Not in this brief

Units; the spin term; the pion; the electron (it keeps no patch open under the working assumption).
