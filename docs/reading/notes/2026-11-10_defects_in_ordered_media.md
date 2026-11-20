# Reading note: flaws in ordered materials (liquid crystals and crystals) as published mathematics for halves, pairs and one-sided loops (10 November 2026)

**Why read:** her question of 10 November on Ashley's crystal page ("crystal seems a good analogy but can it add
to the approach I'm taking ?") and her "Yes proceed" to a note on the published theory of flaws in ordered
materials. The aim is the list of published rules for which flaws exist, which come in halves, which cancel and
which combine, set beside her rules. **Who read:** an assistant session with a fetch agent, 10 November 2026. What
was read in full is marked; the rest is marked abstract, partial or not reached. Nothing here is a result, and a
resemblance is not a confirmation (rule 13). Nothing in `HYPOTHESIS.md` changes.

A word on words: the published field calls these flaws "topological defects". The glossary keeps that term away
from the toy's relic (nothing shows the relic is protected), and this note uses it only for the published
materials.

**The idea in one paragraph (general knowledge; the standard review was not reached, see section 5).** An ordered
material has, at every place, an "order": for a liquid crystal of rod-shaped molecules (a nematic), the direction
the rods point, with no head or tail, so a direction and its reverse are the same order. Collect every possible
order into one space, the order-parameter space. Walk once round a suspected flaw and note the order at each step:
that traces a closed path in the space of orders. If the path cannot be shrunk to a point inside that space, the
flaw cannot be smoothed away, and the kinds of unshrinkable path are the kinds of flaw. How paths combine is how
flaws combine. Everything below is that one idea applied to different materials.

## 1. Layered material in two dimensions: the space of orders is a Klein bottle

**Source read in full (the arXiv text):** B. G. Chen, G. P. Alexander and R. D. Kamien, "Smectics: Symmetry
Breaking, Singularities, and Surfaces", arXiv:0905.3535; the arXiv page gives *Proc. Natl. Acad. Sci.* 106, 15577
(2009), doi:10.1073/pnas.0905242106. A later paper's reference list gives the published title as "Symmetry
breaking in smectics and surface models of their singularities"; the title at the journal is to verify.

A smectic is a liquid crystal whose molecules sit in evenly spaced rows (layers). In two dimensions:

- **The space of its possible orders is a Klein bottle, not a torus** (their section "Defects, Fundamental Groups,
  and All That"). Two things label an order: where the rows sit (a shift, which repeats after one row spacing) and
  which way the rows run (an angle). Rows that carry an arrow would give a torus. Rows carry no arrow, so turning by
  half a turn gives the same rows, and a half turn reverses the direction of every shift: that reversal is the
  Klein bottle's twist.
- **The rule for combining**, their group: two generators, S (a shift by one row) and F (a flip, the half turn),
  with one relation, F S F⁻¹ S = e; in words, carrying a shift through a flip reverses it.
- **Half-strength flaws exist because the rows are one-sided** in this sense (their Fig. 2: +½ and −½; "because
  they are non-orientable"). A flaw of strength ½ is one F.
- **A +½ and a −½ together make a row that ends (a dislocation), or nothing**, depending on how they sit (their
  Fig. 3): at different heights in the rows, the pair is a dislocation; at the same height (a "pincement") the pair
  can be cancelled.
- **A cap, and a failure of the simple rule.** The path-counting above predicts flaws of strength greater than +1;
  Poénaru proved they cannot exist with evenly spaced rows, and the simple rule gives no sign of this. Their reason:
  a smectic has one way to move (the displacement of the rows), not two, so not every path in the space of orders
  can be realized. They replace the rule with a height function over the plane, with row endings as its branch
  points and the half flaws as its critical points; two +1 flaws cannot merge because a saddle lies between them.
  Their energy is their Eq. (1): a term for row spacing (B) and a term for row bending (K₁).

**Exact, ours, from their relation (three lines of algebra, not in the paper in this form; to verify against
section 5's review when it is read).** The relation gives F S⁻ᵏ = Sᵏ F. Then:

- two flips of the same hand, F · F = F², are not nothing and not a shift: a whole flaw (strength 1);
- a flip and its reverse on the same path, F · F⁻¹ = e: nothing;
- a flip and its reverse reached by paths that differ by k rows, (Sᵏ F S⁻ᵏ) · F⁻¹ = S²ᵏ: a shift of 2k rows left
  behind, a row ending. (The paper says the same in its own words: the charge of a row ending is uncertain by two
  in the presence of a half flaw.)

**Set beside her rules (ours, unverified; a resemblance, not a result).**

| Published, for the two-dimensional layered material | Hers |
|---|---|
| Half flaws exist only because the rows are one-sided | Halves make one-sided matter; halves only in two dimensions (step 1; Update 156) |
| Two halves of the same hand make a whole, F² | "combining two same-direction twists into one twist"; a Klein store is two like-handed halves joined (step 1, step 2) |
| Opposite halves cancel, or leave a shift behind | Twist is its own number again: two opposite half twists cancel into light and leave the curl as a dark gluon (6 November, night) |
| Nothing above strength +1 with even rows (Poénaru) | Curl runs from −1 to 1; the dark particle "can take no more curl" (step 1, step 5) |
| The space of orders is a Klein bottle | The Klein bottle is the two-dimensional representation (Update 156) |
| The rows; a half turn reverses the shift | The doughnut's hands "arranged in rows" (step 1) |

**Where the resemblance stops, plainly.** (a) The published Klein bottle is the space of all possible orders, a
piece of bookkeeping; no Klein bottle sits in the material. Her Klein store is an object in the state. Kind of
objection: a theory's structure, not a stopper; but the two must not be written as the same thing. (b) The published
quantities are a shift and a turning; hers are curl and twist. Which of hers is which, if either, is not known;
the table matches rules for combining, not the things combined. (c) The published flaws move; her store cannot.
(d) Her thirds have no counterpart here (section 4).

## 2. One-sided strips force a half flaw to thread them

**Source read in full (the arXiv text):** T. Machon and G. P. Alexander, "Nematics, Knots and Non-orientable
Surfaces", arXiv:1305.0143; the arXiv page gives *Proc. Natl. Acad. Sci. USA* 110, 14174–14179 (2013),
doi:10.1073/pnas.1308225110. Theory and numerical minimization of the standard liquid-crystal energy (their
Methods, Eq. (2)); no experiment of their own.

- A Möbius strip placed in a nematic, the rods meeting its faces at right angles, **must be threaded by a closed
  loop of half flaw**, carrying no point charge (their section 2 and Fig. 2). In cross-section the loop is a −½ on
  the outside of the strip and a +½ on the inside.
- **Parity of half twists** (their Fig. 3): a strip with an odd number p of half twists is one-sided and encloses an
  odd number of half-flaw lines; with p even it is two-sided and encloses an even number. The strip's edge is a
  knot for odd p (p = 3 the trefoil) and two linked loops for even p.
- In general (their section 1): any one-sided surface with an edge forces a flaw that cannot be smoothed away.

**Set beside hers.** Her record's exact fact, "a loop is one-sided exactly when its total twist is an odd number of
halves, so no loop of thirds is one-sided" (`HYPOTHESIS.md`, Dark matter), is the same parity statement. What the
paper adds: one-sidedness is not free in an ordered medium; the medium must carry a half flaw through the strip.
In her words that would read: a one-sided dark loop comes with a line threading it. Whether that line is anything
in her picture (the rod through the stacked one-sided loops is the nearest shape) is hers; ours to flag only.

## 3. Two dimensions keep the sign of a half; three dimensions lose it

**Source read in part** (introduction and sections II.1 to II.3 word for word; sections III to VI through a
summary only, marked S): G. P. Alexander, B. G. Chen, E. A. Matsumoto and R. D. Kamien, "Disclination Loops,
Hedgehogs, and All That", arXiv:1107.1169; *Rev. Mod. Phys.* 84, 497 (2012), doi:10.1103/RevModPhys.84.497.

- **Two dimensions** (their II.1, II.2): the flaws of a nematic are labelled by the half-integers, signed. Two of
  the same sign add; a +½ and a −½ "combine and annihilate each other".
- **Three dimensions** (their II.3): there are only two classes of path, shrinkable and not. So there is one kind
  of half-flaw line, with no sign: a +½ line turns into a −½ line by tilting the rods through the third direction
  (S), two half lines together can be smoothed away (S), and there is no whole-strength line at all (S).
- **Closed loops of half flaw in three dimensions come in four kinds** (stated in Machon and Alexander's
  introduction, citing Jänich and this review): by whether the loop is linked with another flaw an even or odd
  number of times, and whether it carries an even or odd point charge. The detail of how the four combine is S,
  not verified.

**What this means for her picture (kind: a theory's structure; it cannot stop an idea, but it names a question).**
Her dark matter and dark antimatter are half twists of two signs on the face diagonals of three-dimensional space
(step 5). In a headless-rod medium the sign of a half does not survive in three dimensions; it survives in two.
That agrees with her placing the halves' handedness in the two-dimensional doughnut (hands in rows, the two halves
of the doughnut) and asks one thing of the three-dimensional side: what keeps a dark half's sign there. In her
rules the answer may already exist (the sign is the colour of the diagonal, which the wiring fixes; a headless rod
has no colours). Exact test that would tell: on the six-link lattice, whether any allowed move carries a +½ face
loop into a −½ one; not run.

## 4. Crystals: flaws as geometry, and gravity in a flat world

**Source read in part** (abstract, introduction, sections 2 to 7, Table 1, sections 13 to 15 word for word;
sections 8 to 12 and the reference list through a summary, S): M. O. Katanaev, "Geometric Theory of Defects",
arXiv:cond-mat/0407469; *Physics-Uspekhi* 48, 675–701 (2005), doi:10.1070/PU2005v048n07ABEH002027. It reviews
M. O. Katanaev and I. V. Volovich, "Theory of defects in solids and three-dimensional gravity", *Ann. Phys.* 216,
1–28 (1992) (reference as given in the review's list, S; the 1992 paper itself not read; to verify).

- A crystal full of flaws is described as a space with geometry: row-ending flaws (dislocations) are **torsion**,
  "equal to the surface density of the Burgers vector"; turning flaws (disclinations) are **curvature**, "the
  surface density of the Frank vector" (introduction; Table 1; conclusion).
- The equations for a static set of flaws are those of gravity in three dimensions with torsion (S for the detail;
  the abstract and the 1992 title say so).
- Cutting out or adding a wedge makes a cone-shaped point; this review ties the wedge to torsion and calls it a
  wedge dislocation, noting others call it a disclination (S). So the naming of the wedge differs between authors;
  do not quote either as the standard.

**Set beside hers, with one warning.** This is the published "crystal as spacetime" mathematics, and it is the
nearest published form of Ashley's crystal picture that yields equations. The warning: it would be easy to write
"her curl is curvature, so curl is a disclination". The record forbids that as it stands: the toy's surplus square
"is a wrap, not curvature" (`WITHDRAWN.md`, section 3, Update 92). Whether curl or twist is either of the two
published kinds is not known and is not claimed here.

**Thirds.** No source read here has flaws in thirds. General knowledge, to verify: the allowed fractions follow
the symmetry of the order (halves from a two-fold symmetry), so thirds would need an order with a three-fold
symmetry. Her rule that thirds need three dimensions (Update 156) is not addressed by anything read. Open.

## 5. Not reached, and owed

- **N. D. Mermin, "The topological theory of defects in ordered media", *Rev. Mod. Phys.* 51, 591–648 (1979):
  not reached** (the publisher refused the fetch). The reference is as printed in the reference lists of the
  Machon and Alexander paper (read) and the Alexander et al. review (S). It is the standard review of the idea in
  the opening paragraph; that paragraph stays "general knowledge, to verify" until it is read. Chen et al. credit
  the point that combining flaws can depend on the path to Poénaru and Toulouse (1977), not read.
- Poénaru's proof of the cap at +1: cited by Chen et al., not read.
- Kléman, cited by Chen et al. for the group: not read.
- The 1992 Katanaev and Volovich paper: not read.

## 6. What it gives the approach (ours, from the reading)

1. **A published rule-book of the right shape.** For a layered two-dimensional material the published rules have
   halves from one-sidedness, like halves making a whole, opposite halves cancelling or leaving something behind,
   a cap at one, and a Klein bottle as the space the rules live on. Her rules have the same list. That is worth
   one exact look and no more until it has run.
2. **The exact look it suggests** (run the same day in a sharper form, `sandbox/klein_rules_look.py`; the LOG line
   of 10 November is its home: every move of the build is allowed by the published rule, and the build is the
   stricter of the two. The wording below was too loose, since any square grid has both symmetries, and is kept
   as first written.) Does the toy's four-link sheet, with its state on the squares
   (`graphity.curl_pairs`), have the two symmetries that make the Klein bottle: a shift by one row, and a flip
   that reverses the shift? If yes, the published combining rules apply to it by arithmetic and can be checked
   against `graphity.curl_pair_moves` move by move (which moves are F, which are S, whether F · F and the two
   kinds of F · F⁻¹ come out as her store, her cancellation and her dark gluon). If no, the resemblance is words.
   Either answer is quick and decisive, and it should run before any of the table in section 1 is repeated
   anywhere else.
3. **A published energy with two constants** (row spacing and row bending, Chen et al. Eq. (1)), to set beside the
   four factors of the store's energy in the note of 5 November (`2026-11-05_twist_repulsion_dna_mobius.md`).
4. **A question for the three-dimensional side** (section 3): what keeps a dark half's sign in three dimensions.
5. **For Ashley's page:** the crystal picture's published form with equations is section 4; his flaw-seeded snap
   is nucleation at a flaw, which is her loose remnant of 6 November. His rhythm of burps is his own addition.
