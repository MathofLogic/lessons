"""
claims.py — the /lessons ledger, priced by the Atlas LEDGER plate.
==========================================================================
Checked claims name entries in lessons_checks:CHECKS, run by the gate.
What the labs teach is not on this ledger and cannot be: pedagogy is
not a check-backed claim, and pretending otherwise would be the exact
reification the course warns about in lesson one.
"""

SECTIONS = [
    ("The instrument", [
        {"claim": "the vendored kernel is byte-identical to the pinned "
                  "seal: sha256(pl.py)[:16] recomputes to "
                  "bfddc7d82986ba9b",
         "check": "kernel_byte_identity", "tier": "FORCED"},
        {"claim": "the course boots only on a passing kernel self-"
                  "audit: every lab and solution runs against the "
                  "sealed instrument",
         "cite": "README: how grading works; tests/run.py KERNEL SEAL",
         "tier": "CONDITIONAL"},
    ]),
    ("The grading discipline", [
        {"claim": "all nine lessons ship complete: LESSON.md, lab.py, "
                  "solution.py",
         "check": "course_is_complete", "tier": "FORCED"},
        {"claim": "grading is non-vacuous in both directions: "
                  "solutions pass and untouched skeletons fail",
         "check": "grading_is_nonvacuous", "tier": "FORCED"},
    ]),
    ("The sealed history", [
        {"claim": "the committed grading history is a sha-linked "
                  "chain that replays without its writer",
         "check": "history_replays", "tier": "FORCED"},
    ]),
    ("Standing stipulations", [
        {"claim": "a passing build means the course grades what it "
                  "claims to grade — not that the labs teach it, and "
                  "not that PL is the right map",
         "cite": "README non-claims", "tier": "STIPULATED"},
        {"claim": "the lesson sequence and difficulty curve are "
                  "editorial choices, not derived quantities",
         "cite": "tests/run.py non-claims block", "tier": "PRESUMED"},
    ]),
]
