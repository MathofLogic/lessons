# PL-lessons

**The MathofLogic course: analysing, designing, coding, and debugging formal systems with Propagation Logic — every lesson graded by the sealed kernel itself.**

This is not a textbook with exercises. It is nine labs driven by the real
Propagation Logic reference kernel (`pl.py`, vendored byte-identical,
sha256[:16] `bfddc7d82986ba9b`), which **boots only on a passing
self-audit** — the course refuses to run on a kernel that failed its own
enumeration. Every exercise you complete is checked against machinery,
not an answer sheet: your law enumerators are diffed against the kernel's
on all its carriers, your carrier designs are enumerated, your gradients
are driven to decoherence by `propagate`, your witnesses are re-evaluated,
your tampered-chain localiser is tested at every link.

## Who this is for

Engineers. The running examples are health probes, telemetry pipelines,
CI walltime, SLOs, dashboards, audit logs, and one gloriously dishonest
vendor datasheet. No prior logic beyond truth tables is assumed; what is
assumed is that you can read a spec, write a Python function, and care
whether the things you assert are checked.

## How to work

```bash
cd lessons/01_mechanism
cat LESSON.md            # the material  (~10 min read)
$EDITOR lab.py           # fill the TODOs
python lab.py            # grade yourself — FAILs name exactly what's owed
python solution.py       # the reference, when you're done (or stuck)
```

Skeletons fail honestly: an unimplemented exercise reads
`FAIL … (not implemented yet — that's your exercise)`, never a stack
trace. And the course holds itself to a falsifier: `tests/run.py` verifies
in CI that every **solution passes** and every **untouched skeleton
fails** — checks that pass with nothing implemented are vacuous, and
vacuous checks fail the build.

## The arc

**Part I — Analysis** *(reading formal systems)*

| lesson | what you build | what grades it |
|---|---|---|
| **01 · The Mechanism** | `P/G→Q`: loads, θ, decoherence-not-error, `demand()`; pipeline walltime with the load rules | the kernel propagates your predictions to the exact refusal op |
| **02 · The Law Engine** | your own LEM/LNC enumerators; the K3-vs-Ł3 headline (same values, opposite law) reproduced by you | agreement with `enumerate_laws` across all 7 registered carriers |
| **03 · Analysis** | tagging a ten-claim systems spec ([stipulated]/[forced]/[empirical]/[presumed]); the 0.5 test; naming the carrier a coercing dashboard silently presumes | an answer key for the tags; the kernel's own `half_test` verdicts |

**Part II — Design**

| lesson | what you build | what grades it |
|---|---|---|
| **04 · Designing Carriers** | a probe carrier to spec (DN without LEM); buying LEM back and itemising the bill; sweeping the ¬½ dial; a paraconsistent reconciler where a glut doesn't detonate | your tables are enumerated — the design is judged by what it *forces*, not what you meant |
| **05 · Gradients & Cost** | a retry gradient the kernel drives; the group law; the closed loop where value returns and load doesn't; pipeline coherence under θ | numeric verification of state-vs-process; decoherence at the forced op |

**Part III — Coding**

| lesson | what you build | what grades it |
|---|---|---|
| **06 · Through the Gate** | predict PWK's signature, then admit it through the real `register()`; build two carriers that *deserve* refusal (not closed; mis-declared) and watch the gate refuse each | the live registry; the gate's own FORCED refusal claims |
| **07 · DRAS in Code** | metrics as loaded quantities: scope, ledger, priced `reify()`; the 0.5 test as a status-page instrumentation policy; a retention floor with T explicit | the LQ books (loads add, ledgers append, originals stay frozen); `landauer` with no defaulted temperature |

**Part IV — Debugging**

| lesson | what you build | what grades it |
|---|---|---|
| **08 · Debugging Formal Systems** | witnesses (fuzzy LEM at 0.5; probability distributivity at ½,½,½ — 0.375 ≠ 0.4375); fingerprinting three mystery carriers by differential enumeration (one is SQL's `NULL`, which turns out to be K3); `locate_tamper` for sealed chains | witnesses re-evaluated; signatures re-diffed; the localiser tested at all six tamper positions |
| **09 · Capstone** | a full audit of the TriLog™ datasheet (`SPEC.md`): refute "all 15 laws" by enumerating the vendor's own tables, exhibit the LEM witness, fingerprint the product, 0.5-test the "correct: TRUE" badge, DRAS-wrap the bare constant, correct "dropped with an error" to *decoherence with a priced shortfall*, tag all five claims, tier your findings, and compute your audit's own weakest-link composite — which caps at STIPULATED, and you must say why | every finding re-derived: the grader re-enumerates, re-runs the witness, re-checks your weakest link. Nothing you assert is taken on faith — which is the compliment the course has been building to |

## Design commitments

- **The kernel grades; the course doesn't.** Ground truth in every check
  is computed by the sealed kernel at grade time, never hard-coded where
  a computation exists.
- **Both directions in CI.** Solutions pass *and* skeletons fail — the
  course ships its own falsifier.
- **Honest tags for inherited facts.** Where a lesson leans on the
  Atlas's 354,294-carrier enumeration (no 3-valued 15/15; the 14/15
  frontier), it says **[presumed]** and points at /PL's sealed run rather
  than pretending to re-derive it.
- **Fails teach.** Every check name states the property, so a FAIL is a
  lesson, not a scold.

## Repository map

```
pl.py            the sealed kernel (bfddc7d82986ba9b) — the course's instrument
course.py        boot gate + the shared grader
lessons/01…09    LESSON.md + lab.py + solution.py  (09 adds SPEC.md)
tests/run.py     the build gate (seal + both-directions discipline)
.github/         CI runs the gate on every push and PR
```

## Relation to the other MathofLogic repos

**/PL** is the framework this course teaches — kernel, atlas, DRAS, all
sealed. **/rigor** is the same discipline industrialised into audit
tooling for code and papers. This repo is the on-ramp: finish the
capstone and both of those codebases read as applied exercises.

## License

MIT. Trust infrastructure should not be paywalled — and neither should
learning to build it.
