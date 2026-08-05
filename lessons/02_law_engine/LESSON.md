# Lesson 02 — Carriers and the Law Engine

*The most important sentence in the framework: **a law is a property of
`G` on `V`, not a fact to look up.***

## Carriers

A **carrier** is a value space with its machinery: `(V, neg, AND, OR, D)`,
where `D ⊆ V` is the *designated* set — the values that count as "asserted".
Classical logic is the carrier `V={0,1}, D={1}` with the familiar tables.
Strong Kleene (K3) is `V={0,½,1}, D={1}` with `min/max` and `¬½=½`.
That `½` is not "sort of true" — it is *no information yet*: the timed-out
probe, the pending check, the unparsed field.

## Laws are outputs

Ask "does the law of excluded middle hold?" and most training says: look
it up. The kernel's answer: **enumerate it.** For finite `V`, every one of
the 15 classical laws is *decided* by complete enumeration — LEM is just
`all(OR(a, neg(a)) ∈ D for a in V)`, checked over every value. No axioms.
No authority. The tables force the answer.

The 15, by their kernel keys: `LNC, LEM, DN, NoGlut, MP, ANDcomm, ORcomm,
ANDassoc, ORassoc, ANDidem, ORidem, DeM1, DeM2, Distrib, Absorb`.

## The headline you will reproduce

K3 and Łukasiewicz-3 (Ł3) have **exactly the same value space**,
`V = {0, ½, 1}`, the same negation, the same designated set. They differ
only in the gradient: K3 uses `min/max`, Ł3 uses `max(0,a+b−1) / min(1,a+b)`.
Enumerate both and LEM **fails** in K3 (`OR(½,¬½) = ½ ∉ D`) yet is
**forced** in Ł3 (`OR(½,½) = min(1,1) = 1`). Same values. Different
machinery. Opposite law. That is why "which logic does this system assume?"
is an engineering question with a computable answer — and why in Lesson 08
you will *debug* systems by enumerating what their tables actually force.

## Signatures and their price

A carrier's **signature** is its full 15-law vector. No 3-valued carrier
reaches 15/15 (the Atlas in /PL enumerated the entire 354,294-carrier
space to prove it) — every signature *pays* for what it keeps. K3 pays LEM.
Ł3 buys LEM back and pays idempotence, distributivity, absorption. LP
designates the glut and pays detachment (MP). Design, in Lesson 04, is
choosing which bill to run up.

## The lab

You will write your own enumerators for LEM and LNC and be graded against
the kernel's `enumerate_laws` on every registered carrier; then reproduce
the K3/Ł3 headline; then compute the exact law-set on which two carriers
differ.
