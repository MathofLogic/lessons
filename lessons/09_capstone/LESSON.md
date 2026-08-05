# Lesson 09 — Capstone: Audit a Formal System End-to-End

*Everything converges. You are handed `SPEC.md` — a vendor datasheet for
"TriLog™" — and you will do to it what this course trained you to do:
analyse, enumerate, witness, tag, price, and seal.*

## The brief

Produce a full audit of the five claims T1–T5. Your `audit()` returns a
manifest — findings, not verdicts on the vendor's soul — and the grader
holds every finding to the kernel:

1. **T1 vs T2 (Lesson 02, 06, 08).** The vendor asserts all fifteen laws;
   the vendor also publishes normative tables. Tables outrank prose:
   **enumerate T2** and count. Report `laws_held`, the exact set of laws
   sacrificed, and — corpus method — a concrete **witness** for one
   failure (the value at which LEM dies, and what OR(a, ¬a) evaluates to
   there). Fingerprint bonus: which registered carrier is TriLog really?
2. **T3 (Lessons 03, 07).** "Your pipeline is correct: TRUE." Run the 0.5
   test. Correctness of a pipeline is graded; a binary badge is a
   reification with an undisclosed threshold. Tag the claim and attach the
   kernel's verdict string.
3. **T4 (Lesson 07).** `K = 42` — units unstated, method unstated,
   baseline unstated. A bare constant is a quantity with its history
   erased. DRAS-wrap it: return an LQ whose scope discloses at least
   units and method (your reconstruction, honestly labelled as such).
4. **T5 (Lessons 01, 05).** "Over-budget decisions are dropped with an
   error." Half right. Model a decision under θ with the kernel and
   report the correction: over-budget is **decoherence** — flagged,
   priced (`demand()`), unusable — not an error, and the datasheet's
   framing erases the bill. Include the decoherence op for the concrete
   case: 30-per-step load, θ = 100.
5. **The verdict (everything).** Tag T1–T5, tier your own findings
   (FORCED for enumerations and witnesses, STIPULATED for 0.5-test
   verdicts, and so on), and compute the audit's composite tier by
   **weakest link over your non-UNPAID findings** — then note, in the
   manifest, why the composite cannot outrank STIPULATED.

## The shape of the deliverable

`audit()` returns a dict; `lab.py` documents the exact keys. The grader
re-enumerates your enumeration, re-runs your witness, re-checks your
weakest link. Nothing you assert is taken on faith — which, by this
point in the course, is precisely the compliment.
