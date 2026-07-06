# Source notes — provenance of /PL-lessons

Built 2026-07-06 as the third standalone MathofLogic repo, alongside /PL
(the framework) and /rigor (the audit tooling).

## Inherited, byte-identical

- `pl.py` — the reference kernel, sha256[:16] `bfddc7d82986ba9b`, vendored
  unmodified from /PL. The build gate pins this hash; the course teaches
  against a specific sealed instrument, and a drifted kernel is a
  different course.

## Written for this repo (all gated)

- `course.py` — the boot gate (kernel must pass its full self-audit
  before any lesson runs; exec'd in a scratch cwd so manifest writes
  never touch the repo) and the shared grader (NotImplementedError is a
  named FAIL, not a crash — skeletons fail pedagogically).
- Nine lessons: LESSON.md + lab.py + solution.py each; the capstone adds
  SPEC.md (the TriLog datasheet under audit).
- `tests/run.py` — enforces the seal and the both-directions discipline:
  every solution exits 0, every untouched skeleton exits nonzero. The
  second direction is the course's own falsifier: checks that pass with
  nothing implemented are vacuous, and vacuous checks fail the build.

## Defects caught by the course's own gates during authoring

Recorded because the discipline says so:

1. Lesson 05's group-law check originally staged the second leg from E0
   instead of E1 — the reference solution failed the reference check,
   which is exactly what running both directions is for. Fixed in the
   check.
2. Lesson 09's weakest-link check was first written in an unreadable
   double-negative form; rewritten before it could hide a bug.
3. Lesson 06's PWK signature was predicted before enumeration (LNC=F,
   LEM=T, DN=T, MP=F) and the gate confirmed 11/15 with exactly that
   four-law face — the predict-then-enumerate method, demonstrated on
   the author.

## Deliberate non-claims

- The Atlas frontier facts used in Lessons 04/08 (no 3-valued 15/15;
  signatures don't individuate) are [presumed] from /PL's sealed
  354,294-carrier run (`ab59172abd6618cb`), not re-derived per lab.
- The answer key in Lesson 03 is a STIPULATION of the course (tags on
  prose are judgment calls at the margin); the check therefore requires
  8/10 agreement plus the two unambiguous presumptions, not 10/10.
