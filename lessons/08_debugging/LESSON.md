# Lesson 08 — Debugging Formal Systems

*A formal system is debugged the way a program is: reproduce the failure,
minimise it to a witness, localise it structurally. The tools are the
corpus method, differential enumeration, and chain replay.*

## Technique 1 — the corpus method (counterexamples as artifacts)

For continuous carriers, laws can't be settled by finite enumeration —
they are property-tested, and a failed law is **proved by a single
exhibited counterexample**. The witness is the deliverable. Two classics
you will reproduce:

- Fuzzy LEM: `OR(x, 1−x)` should always be 1 if LEM held; at `x = 0.5` it
  is `max(0.5, 0.5) = 0.5`. One point, law dead — and 0.5 is the *maximal*
  witness, the point of deepest failure.
- Probability distributivity: with `AND = ab`, `OR = a+b−ab`,
  `a∧(b∨c)` vs `(a∧b)∨(a∧c)` at `a=b=c=½` gives `0.375 ≠ 0.4375`. Note
  what this debugs in real systems: anyone refactoring alerting rules or
  probabilistic feature-gates *as if* Boolean algebra applied is applying
  distributivity to a carrier that does not have it.

A witness beats an argument. In a design review, "distributivity fails"
invites debate; "at a=b=c=0.5 the two sides are 0.375 and 0.4375" ends it.

## Technique 2 — differential enumeration (which carrier is this?)

Symptom-driven diagnosis: you are handed a mystery system's tables — a
vendor's "TriBool" type, an ORM's NULL semantics, a legacy rules engine —
and must identify what logic it actually is. Method: enumerate its 15-law
signature and diff against the known registry. The signature is a
fingerprint. (One honest caveat, inherited from the Atlas: signatures
don't *individuate* — RM3 and LP share one — so the fingerprint narrows
to an equivalence class, which for debugging is almost always enough.)

SQL's `NULL` is the canonical mystery: `NULL AND FALSE = FALSE`,
`NULL OR TRUE = TRUE`, `NOT NULL = NULL` — enumerate it in the lab and
watch K3's signature appear. Your database has been running strong Kleene
since 1986; most code above it assumes CL2. That mismatch is a standing
production bug factory, and now you can name it.

## Technique 3 — chain replay (localise the tamper)

Sealed histories (every suite in /PL ends with one) turn "someone edited
the audit log" from a suspicion into a **located fact**: each generation's
hash commits to the previous, so a mutation breaks replay *at its link* —
not somewhere, there. You will implement the localiser: given a tampered
chain, return the exact index where trust ends.

## The lab

Exhibit both classic witnesses; fingerprint three mystery carriers
(one of them is SQL's NULL) by differential enumeration; and write
`locate_tamper` for sealed chains.
