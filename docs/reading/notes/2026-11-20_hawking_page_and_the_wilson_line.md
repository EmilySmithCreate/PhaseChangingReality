# Reading note: the Hawking-Page transition, the reading of light round a curled direction, and what carries over to the toy (20 November 2026)

**Why read:** her question of 20 November on Anthropic's page "Claude solves two open problems in the physics of
black holes" (17 November 2026), then her "proceed with the research and see if the math helps us understand or
refine my hypothesis" (both verbatim in `sandbox/NOTEBOOK.md`). **Who read:** this session, 20 November 2026.
**What she is after:** published mathematics she can apply to her picture; not a confirmation of anything (rule 13).
Every reading of ours below is ours, unverified by any physicist.

## What was read, and how deeply

| Source | Read | Used for |
|---|---|---|
| Aharony, Marsano, Minwalla, Papadodimas, Van Raamsdonk, "The Hagedorn/deconfinement phase transition in weakly coupled large N gauge theories", Adv. Theor. Math. Phys. 8 (2004) 603, arXiv hep-th/0310285 ("AMMPV") | **In part, from its TeX source (v6):** sections 1, 5.7, 6.3, 7.3, and the opening of 2.1 | The method; the one-number criterion; the filled-in circle |
| Same authors, "A first order deconfinement transition in large N Yang-Mills theory on a small 3-sphere", Phys. Rev. D 71 (2005) 125018, arXiv hep-th/0502149 | Abstract only (by an assistant agent) | The lowest order sits on the borderline |
| "The Hawking-Page transition at weak coupling", hexagonmath.org/2611.00175v1 (7 November 2026, 42 pages, author line "Claude (Anthropic)", labeled primarily AI-generated, checked by one physicist against special cases; not peer reviewed as far as its page says) | **In part, from the PDF's text:** sections 1.1 to 1.3, 7.1, 7.2, and the caveat closing section 6 | The new number; the three saddle points |
| Witten, "Anti-de Sitter space, thermal phase transition, and confinement in gauge theories", Adv. Theor. Math. Phys. 2 (1998) 505, arXiv hep-th/9803131 | **In part:** introduction, sections 2.1 (by an assistant agent), 3.2 and the end of 4 (PDF text) | Which geometry has the circle filled in; what that does to bonds |
| Maldacena and Strominger, "AdS3 black holes and a stringy exclusion principle", JHEP 9812:005 (1998), arXiv hep-th/9804085 | **In part:** section 3.3, Eqs. (3.15) to (3.23) (PDF text) | The black hole and the hot gas in three dimensions |
| Bañados, Teitelboim, Zanelli, "The black hole in three dimensional space time", Phys. Rev. Lett. 69 (1992) 1849, arXiv hep-th/9204099 | Abstract only (by an assistant agent) | Negative vacuum energy |
| Carlip, "Lectures in (2+1)-dimensional gravity", J. Korean Phys. Soc. 28 (1995) S447, arXiv gr-qc/9503024 | Sections 1 and 2's opening (by an assistant agent) | No waves in two space directions |
| "The spinless modular bootstrap at large central charge", hexagonmath.org/2611.00174v1 (131 pages) | Abstract only | The page's second result; not used further |
| 't Hooft, "A two-dimensional model for mesons", Nucl. Phys. B75 (1974) 461 | **Not retrieved** (publisher refused, INSPIRE returned nothing) | Still general knowledge, to verify |
| Deser, Jackiw, 't Hooft (1984), point masses in three-dimensional gravity | **Not read** (named by Carlip, section 1) | Still general knowledge, to verify |

Symbols: their λ is 't Hooft's coupling, not the toy's curling knob; their N is the number of colors, not the
toy's number of points.

## The published method, in plain words

**The setting** (AMMPV section 1; Witten introduction, footnote 1). A quantum theory at temperature T is computed on
a space with one extra direction curled into a circle of length 1/T. The theory studied has light of many colors
(N of them) on a small round space.

**The one object** (AMMPV abstract and section 1). Everything heavy is summed away and one thing is left: what the
light field reads going once round that circle, "the holonomy (Wilson loop) of the gauge field around the thermal
time circle". Call its size u (their |u₁|, between 0 and ½).

**The one number** (AMMPV section 6.3, their equation for S_eff(u₁)). Near the transition the energy of the reading is

    S = N² ( m² u² + b u⁴ ),     m² falling through zero as the temperature rises through T_H.

If b > 0 the reading grows smoothly from zero: two smooth transitions. If b < 0 the reading jumps from 0 to ½ a
little below T_H: one abrupt transition. With no forces at all the energy is exactly flat at the transition (the
preprint, section 1.3: "exactly flat at the transition, and the order parameter jumps because nothing opposes it"),
and the 2005 abstract says the lowest order sits "precisely on the borderline", so b had to be computed at the third
order.

**The new number** (the preprint, section 7.1, Eq. 64): b = −1.481 × 10⁻³ λ², negative: abrupt. Its own caveat
(end of section 6): some coefficients of one piece were produced by one of its two programs only; they contribute
−0.34 of −1.50 in its units, and the sign's margin is fourteen in those units.

**Three arrangements, three temperatures** (the preprint, section 7.2; AMMPV section 6.3). Below T_min only the
reading-zero arrangement exists. Between T_min and T_H there are three: reading zero (the hot gas), an unstable one
(the small black hole, the top of the wall), and reading about ½ (the large black hole). The first and third
exchange which is cheaper at T_c. At T_H the unstable one merges with the first, which stops existing. The window
is narrow: one part in ten thousand at λ = 1.

**What the reading means** (AMMPV section 7.3; Witten section 2.1; the preprint, section 1.1). The reading "clearly
vanishes if the Euclidean time circle is non-contractible", and "we take the vanishing of the Polyakov loop to be
the definition of a non-contractible circle"; a circle that can be shrunk to a point, filled in, goes with a
horizon, so "suitably defined Polyakov loops are non-zero only in a black hole phase". Witten: in the hot-gas
geometry the circle "is not the boundary of any D"; in the black-hole geometry it is the boundary of a disc.

**What needs many colors** (AMMPV section 1). With one color the particles of light are free in any number; with
many colors only color-neutral groups are allowed on a closed space, and that restriction alone makes the
transition. "For finite N, this phase transition is smoothed out, as it must be for any theory with a finite number
of degrees of freedom at finite volume." The many-color number N² is also the count of the black hole's states on
the gravity side (the preprint, section 1.1: the jump is from order one to order N², and 1/G_N ∼ N²).

**The same filled-in circle, read two ways** (Witten sections 3.2 and 4). In the geometry with the circle filled
in, a charge whose path runs round the circle is free (the reading is non-zero), while two charges separated in
the *other* directions are held by a bond whose cost grows with the area between their paths, "an area law for
spatial Wilson loops", because the surface between them cannot go below the place where the circle closes. Section
4 reads the filled-in circle as a small direction of space and gets, in the world one dimension lower, bonds that
do not let go and a lowest mass ("a confining theory with a mass gap").

**Three dimensions** (Maldacena and Strominger, Eqs. 3.16, 3.20). With two space directions the boundary is a
doughnut; the black hole and the hot gas are two solutions whose costs are exchanged by τ → −1/τ, the exchange of
the doughnut's two circles, and a whole family of solutions follows from the other exchanges (Eq. 3.21).

## The three statements marked "to verify" on 20 November, now

1. *Temperature is a direction curled into a circle.* **Sourced:** Witten, introduction, footnote 1 ("path
   integrals on R³ × S¹, with a radius for the S¹ equal to β = T⁻¹"); AMMPV section 4.
2. *'t Hooft's 1974 two-dimensional model is solved in the limit of many colors and binds with a bond linear in
   separation.* **Still general knowledge, to verify:** the paper was not retrieved. The preprint (section 1.2)
   credits 't Hooft with "the limit of many colours", citing a different paper.
3. *Einstein's gravity with two space directions: no waves; black holes with negative vacuum energy; no pull
   between resting masses.* **Sourced in part:** no local degrees of freedom and no gravitational waves (Carlip,
   section 2); the black hole solution exists "with a negative cosmological constant" (BTZ abstract; it says
   "admit", not "require"). **Not sourced:** no pull between resting masses (Deser, Jackiw and 't Hooft 1984, not
   read).

## What the look found (`sandbox/LOG.md`, 20 November; one home)

`sandbox/wilson_line_look.py`, on the toy's built lattice light (term 10, which is not her light).

## What it is and is not for her picture (ours, unverified)

- **The recipe itself does not carry over to the toy's light.** With one phase the loop's potential on a fixed
  wiring is a single well at every stiffness (exact), and the published reason is above: one color has no
  restriction to neutral groups. The jump in the toy is in the wiring; the loop only reports it.
- **What carries over is the criterion.** In the toy a loop's reading is non-zero exactly when the loop is filled
  in by squares (exact), and a loop round a curled direction filled by a square is what a surplus square, her curl,
  is. The published definition of the black-hole side is the same filling-in.
- **Not her light, not our sky, not her loop.** Term 10 lives on the links; her light travels the body diagonals.
  Every published statement here is in a spacetime with negative vacuum energy. Nothing read has a daughter, a
  burp into a new space, matter against antimatter, or dark matter.
- **Still owed:** sources for statement 2 and the last part of 3; the published list of flat three-dimensional
  spaces behind the look's Part 6 (Conway and Rossetti, "Describing the platycosms", arXiv math/0311476, named
  from memory, not read: general knowledge, to verify).

## Added later on 20 November, for her answers of the same day (notebook, "20 November 2026, later")

**Readings in N-ths of a turn** (AMMPV section 2.2, read from the TeX source). With N colors, "𝒫 → e^{2πi/N} 𝒫 is
a symmetry of the SU(N) Yang-Mills path integral", "spontaneously broken in the deconfinement phase transition";
section 6.1 derives the same for the effective action ("S_eff should be invariant under U → e^{2πik/N} U"). So
with three colors the theory is unchanged when the loop's reading is turned by a third of a turn. This is the
nearest published object to "a loop read in thirds". The second look (`sandbox/electron_triangle_look.py`, the LOG
line of 20 November, later) is on wirings only and uses none of it.

**Named from memory, not read: general knowledge, to verify, owed within the week (rule 19).**

- *(Read the same evening; see the next section.)* That quark charges in thirds are tied to the three-color rule
  through the way the forces' groups are joined (Tong 2017).
- That the middle of Kerr's rotating black hole is a ring whose radius is the angular momentum per unit of mass
  (Kerr 1963; a textbook or Visser, "The Kerr spacetime: a brief introduction", arXiv 0706.0622).
- That a solid doughnut fills in its short-way circle and the space outside it fills in the long-way one (a
  textbook of topology; the three-sphere as two solid doughnuts).
- That a Klein bottle is two Möbius strips joined along their edges: exact on the toy's wiring in the second
  look's Part 4; a textbook source still to name.

## Added in the evening of 20 November: charge in thirds and the three colors (her "important and foundational")

Read from the arXiv TeX source, in part, by this session.

- **R. Foot, H. Lew, R. R. Volkas, "Electric charge quantization", J. Phys. G 19 (1993) 361, arXiv hep-ph/9209259.**
  Read: abstract, sections 2 and 3, the close of section 6. Section 3 takes one family of quarks and leptons with
  unknown charge numbers y1 to y5 (Eq. 9; y1 the quark pair, a color triplet; y4 the lepton pair). The mass terms
  fix three of the five (Eq. 10). Two consistency conditions fix the rest: "y1 = − y4/3 and y4 = −1" (Eq. 12).
  "Thus for the Toy Model case of the MSM restricted to only one generation we see that the consistency conditions
  of gauge invariance of the Yukawa Lagrangian and anomaly cancellation uniquely imply that electric charge is
  quantized. Not only is it quantized, but the quarks and leptons have the correct electric charges." The three
  in Eq. (12) comes from the quark's three colors (general knowledge of how the sum is formed; not quoted from the
  paper). **Its own caveat** (abstract; section 5): with three families and massless neutrinos the charges are
  no longer forced, because differences of the family lepton numbers can be mixed in.
- **D. Tong, "Line operators in the Standard Model", JHEP 07 (2017) 104, arXiv 1705.01853.** Read: abstract,
  introduction, the opening of section 2 and its Z6 case, the electromagnetic paragraph of section 3. The forces'
  group is U(1) × SU(2) × SU(3) divided by a subgroup of Z6 "which cannot be determined by current experiments".
  For the full Z6: "the Abelian charge is q = 3 z2 − 2 z3 mod 6. It is noticeable that all fundamental fermions in
  the Standard Model obey this relationship", with z3 = 0, 1, 2 the color class and z2 = 0, 1 the weak class; the
  table gives the electron (0, 0) with q = −6 and the quarks (·, 1) with q = +1, +4, −2. After the weak force's
  symmetry breaks: "The minimum electric charge is Q = 1/3". A minimum magnetic charge then "is inconsistent with
  the fractional charge of the quarks" unless it also carries color.
- **Y.-B. Yang and colleagues, "Proton mass decomposition from the QCD energy momentum tensor", Phys. Rev. Lett.
  121, 212001 (2018), arXiv 1808.08677.** Abstract only (by an assistant agent): quark energy 33(4)(4) %, glue
  field energy 37(5)(4) %, a quarter of the trace anomaly 23(1)(1) %, the quark scalar condensates 9(2)(1) %.

**For her picture (ours, unverified).** Published: a charge in thirds goes with a color class, and the electron's
whole charge is three quark thirds because of a consistency condition with the number of colors in it. Hers: three
thirds on one loop of box diagonals. Same arithmetic, different mechanism; a target, not a confirmation (rule 13).
**Still general knowledge, to verify:** the masses of the Δ (1,232 MeV) and the neutron used in the notebook
(Particle Data Group); the half-turn space and the Klein bottle times a circle in the published list of flat
three-dimensional spaces.

## Added in the night of 20 November: measured masses and the quark model, for her "translate my hypothesis"

Read from the PDFs' text by this session (pypdf in the scratchpad); all are S. Navas et al. (Particle Data Group),
Phys. Rev. D 110, 030001 (2024).

- **Baryon summary table** (`pdg.lbl.gov/2024/tables/rpp2024-sum-baryons.pdf`). Read: the proton, neutron,
  Δ(1232), Δ(1950), Δ(2420), Σ(1385), Ξ(1530) and Ω⁻ entries. Proton 938.27208816 MeV, charge radius
  0.8409 ± 0.0004 fm; neutron 939.5654205 MeV, magnetic moment −1.9130427 nuclear magnetons, mean-square charge
  radius −0.1155 ± 0.0017 fm²; Δ(1232) "Breit-Wigner mass (mixed charges) = 1230 to 1234 (≈ 1232) MeV", full
  width "114 to 120 (≈ 117) MeV", N π 99.4 %; Δ(1950) 7/2+ ≈ 1930; Δ(2420) 11/2+ ≈ 2450; Σ(1385)⁻
  1387.2 ± 0.5; Ξ(1530)⁻ 1535.0 ± 0.6; Ω⁻ 1672.45 ± 0.29, "Ω⁻ = s s s".
- **The Δ(1232) listing** (`.../listings/rpp2024-list-Delta-1232.pdf`). Read: the mass blocks. Separate charge
  states are listed under "We do not use the following data for averages": Δ⁺⁺ 1230.55 ± 0.20 and Δ⁰
  1233.40 ± 0.22 (Gridnev 2006); "m Δ⁰ − m Δ⁺⁺" 2.86 ± 0.30. No separate Δ⁻ mass is listed.
- **Light-meson summary table** (`.../tables/rpp2024-sum-mesons.pdf`). Read: ρ(770) 775.26 ± 0.23; a₂(1320)
  1318.2 ± 0.6; ρ₃(1690) 1688.8 ± 2.1; a₄(1970) 1967 ± 16.
- **Review "Quark Model"** (`.../reviews/rpp2024-rev-quark-model.pdf`, revised August 2023, Amsler, Crede,
  DeGrand). Read: section 15.1 and passages of 15.5 and 15.7. "QCD is believed to confine, that is, its physical
  states are color singlets"; mesons are a quark and an antiquark, baryons three quarks, "coupled into a color
  singlet"; "The color part of the baryon wave function is an SU(3) singlet, a completely antisymmetric state of
  the three colors"; ground-state masses agree with "harmonic (or linear) confinement and a spin-spin
  interaction, which is responsible for the octet - decuplet mass shifts".
- **An encyclopedia page on the Δ** (en.wikipedia.org/wiki/Delta_baryon, by an assistant agent): the four charge
  states, their quark content, the decays, the lifetime (5.63 ± 0.14) × 10⁻²⁴ s as a conversion of the width, and
  the discovery "at the University of Chicago cyclotron and the Carnegie Institute of Technology
  synchro-cyclotron in the mid-1950s". Secondary; the numbers used are the Particle Data Group's.

**Still general knowledge, to verify (rule 19):** the strong force's string tension (about 0.9 GeV per fermi) and
the spinning string's slopes (1/(2π tension) open, half that closed); that the Δ⁺⁺ prompted color historically;
that the decuplet's equal spacing predicted the Ω⁻; the three colors' charges as three vectors at a third of a
turn and the gluons' as their differences; the collider limits on the electron's size.

## Added later on 20 November: the bag model (her "read and proceed")

- **K. Johnson, "The M.I.T. bag model", Acta Physica Polonica B6 (1975) 865–892** (lectures, XV Cracow School of
  Theoretical Physics, Zakopane, June 1975; open access at the journal). A scan with no text layer; read as page
  images by this session: pp. 865, 866, 882, 885, 888, 889, 890. Not read: the rest, including where his μ is
  defined.
  - p. 866: empty space as a medium; "When we locally disturb this medium, we may excite a 'collective' motion of
    some underlying 'stuff' which is present everywhere in its ground state ... The localized excitation will be a
    'particle', a hadron."
  - p. 888, Eq. (4.24): the spin term goes as [n(n − 6) + S(S + 1) + 3I(I + 1)] over R; "It is interesting that
    this is negative only for the nucleon". Eq. (4.25): the mass as valence quark kinetic energy, plus "BV − Z0/R"
    (zero point energy), plus the color interaction energies; "We then minimize (4.25) with respect to R to
    determine the radius of the state". "The free parameters are B, m, m_s, Z0 and α_c", fitted to "the Δ, N and
    ω", with m_s from the Ω⁻.
  - p. 885: with all quarks in the same mode the color electric field "is proportional to the total color operator
    and hence vanishes"; "the main effect of the color gluon interaction is associated with the color-magnetic
    interaction".
  - p. 889, Table I: B^(1/4) = .145 GeV, Z0 = 1.84, α_c = .55, m_s = .279 GeV; the proton row (.938, R0 5.00,
    −.367, .234, 1.226, −.155, 0), the Δ row (1.236 measured, 1.233, 5.48, −.336, .308, 1.119, .141, 0), the pion
    (.139 measured, .280).
  - p. 890: "a total of nine masses ... in generally quite good agreement"; "The mean square charge radius for the
    proton comes out to be 0.73 fm, in comparison with the experimental value, 0.88 ± 0.03 fm. Thus, our proton is
    somewhat too small"; the formula with 2.04/R used in `sandbox/bag_look.py`.
- **The 1974 and 1975 papers** (Chodos, Jaffe, Johnson, Thorn, Weisskopf, Phys. Rev. D 9, 3471; Chodos, Jaffe,
  Johnson, Thorn, Phys. Rev. D 10, 2599; DeGrand, Jaffe, Johnson, Kiskis, Phys. Rev. D 12, 2060): abstracts only,
  by an assistant agent from the INSPIRE record, paraphrased. The first: a hadron as a finite region with a
  "constant energy per unit volume, B"; the second: "The only parameter of the model is fixed by the average mass
  of the N(938) and Δ(1236)".

## Added on 20 November: corrections to the bag model, and the proton's lifetime

Abstracts only, by an assistant agent from the INSPIRE records and one arXiv page, paraphrased with short quotes:

- J. F. Donoghue, K. Johnson, "The pion and an improved static bag model", Phys. Rev. D 21, 1975 (1980):
  wave-packet methods for the localization of the quarks; "These methods have little effect on heavy states";
  expanding about the limit of exact handedness symmetry, a light-quark mass of 33 MeV and F_π about 145 MeV
  against 93 measured.
- S. Théberge, A. W. Thomas, G. A. Miller, "The cloudy bag model. 1. The (3,3) resonance", Phys. Rev. D 22, 2838
  (1980): a pion field coupled to the quarks at the bag's surface; "a bag radius of about 0.72 fm".
- A. W. Thomas, S. Théberge, G. A. Miller, "The cloudy bag model of the nucleon", Phys. Rev. D 24, 216 (1981):
  one free number, the bag radius, about 0.8 fm; radii, magnetic moments and g_A agree very well with experiment;
  "about one-third of the Δ-nucleon mass splitting" from pions.
- G. E. Brown, M. Rho, "The little bag", Phys. Lett. B 82, 177 (1979): pions outside a small bag.
- S. Dürr and colleagues, "Ab-initio determination of light hadron masses", Science 322, 1224 (2008),
  arXiv 0906.3599: a direct computation on a grid; results agree with experiment with controlled uncertainties.
- A. Takenaka and colleagues (Super-Kamiokande), Phys. Rev. D 102, 112011 (2020): "No candidates have been found
  for" a proton turning into a positron and a pion; lifetime over branching fraction above 2.4 × 10³⁴ years.

Read by this session: the Particle Data Group's 2024 baryon summary table, proton decay modes, "N → e⁺ π
> 5300 (n), > 24000 (p)" in units of 10³⁰ years, 90 % confidence.

**Still general knowledge, to verify:** that empty space is a filled state whose energy for every bit of volume
is the bag's constant, and that the same state squeezes the force into strands; that every matter particle has
spin ½ and every carrier spin 1; the unified theories of 1974 in which the proton decays.
