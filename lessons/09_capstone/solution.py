#!/usr/bin/env python3
"""Lesson 09 — reference solution: the full TriLog(tm) audit."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab
from lab import (V3, Z, H, U, trilog_neg, trilog_and, trilog_or, trilog_D,
                 TIER_ORDER)

pl = kernel()


def audit():
    # ── T1 vs T2: tables outrank prose. Enumerate what was published. ──
    laws = pl.enumerate_laws(V3, trilog_neg, trilog_and, trilog_or,
                             trilog_D)
    held = sum(laws.values())
    sacrificed = {k for k, v in laws.items() if not v}
    # corpus method: the concrete point where LEM dies on these tables
    witness = {"law": "LEM", "at": H,
               "evaluates_to": trilog_or(H, trilog_neg(H))}   # = 1/2, not in D
    # differential enumeration: whose signature is this?
    fingerprint = next(k for k, c in pl.REGISTRY.items() if c.laws == laws)
    # (spoiler the grader confirms: K3. TriLog(tm) is strong Kleene
    #  wearing a trademark — a fine logic, dishonestly advertised.)

    # ── T3: "your pipeline is correct: TRUE" ───────────────────────────
    # Correctness of a pipeline is graded (which paths, which inputs,
    # within what tolerances?). Half-correct is coherent, so the binary
    # badge is a reification: someone chose a threshold and erased it.
    # The claim as printed is a stipulation dressed as a property.
    t3 = {"tag": "stipulated",
          "verdict": pl.half_test("pipeline correct", True)}

    # ── T4: K = 42, history erased ──────────────────────────────────────
    # DRAS-wrap the bare constant. The scope below is a RECONSTRUCTION —
    # labelled as such in the ledger — because the vendor disclosed none.
    t4 = pl.LQ(42.0, L=1.0,   # it arrives already owing one distinction:
               # its scope was erased upstream, by the datasheet
               scope=(("units", "seconds (reconstructed, not stated)"),
                      ("method", "unstated; assumed steady-state tuning"),
                      ("baseline", "unstated")),
               ledger=("seeded from SPEC.md T4",
                       "scope reconstructed by auditor — vendor stated none"))

    # ── T5: "dropped with an error" — half right, bill erased ──────────
    ctx = pl.Context(theta=100.0)
    G = lambda P, ctx=None: pl.Pattern(P.v, P.L + 30.0)
    P, op = pl.Pattern("decision", 0.0), 0
    while P.available:
        op += 1
        P = pl.propagate(P, G, ctx)
    t5 = {"correction": "decoherence", "op": op,
          "demand": P.demand(100.0)}
    # op 4: 120 > 100. Not an "error": a refusal, flagged, priced 20,
    # unusable downstream. The datasheet's framing erases the shortfall,
    # which is exactly the number capacity planning needs.

    # ── the tag sheet ───────────────────────────────────────────────────
    tags = {
        "T1": "stipulated",   # an assertion contradicted by the vendor's
                              # own stipulated tables; as a claim about
                              # the product it is a (false) stipulation
                              # of marketing, refuted FORCED above
        "T2": "stipulated",   # tables are a convention — the honest part
        "T3": "stipulated",   # undisclosed threshold dressed as property
        "T4": "stipulated",   # a chosen constant, scope erased
        "T5": "conditional",  # true GIVEN a budget the datasheet never
                              # states; and mis-framed (see correction)
    }

    # ── the audit grades itself ─────────────────────────────────────────
    findings_tiers = [
        "FORCED",       # the enumeration (T1 refutation)
        "FORCED",       # the LEM witness
        "FORCED",       # the fingerprint (signature equality)
        "STIPULATED",   # the 0.5-test verdict on T3 (a heuristic, owned)
        "STIPULATED",   # the DRAS reconstruction of T4's scope
        "FORCED",       # the decoherence op and demand (T5)
        "UNPAID",       # NOT claimed: that TriLog misbehaves at runtime —
                        # only that its datasheet misdescribes its tables
    ]
    composite = max((t for t in findings_tiers if t != "UNPAID"),
                    key=TIER_ORDER.index)
    self_note = ("The audit leans on the 0.5 test and a reconstructed "
                 "scope — stipulations of its own — so by weakest link "
                 "its composite cannot outrank STIPULATED; findings, "
                 "not verdicts.")
    return {"laws_held": held, "sacrificed": sacrificed,
            "witness": witness, "fingerprint": fingerprint,
            "t3": t3, "t4": t4, "t5": t5, "tags": tags,
            "findings_tiers": findings_tiers, "composite": composite,
            "self_note": self_note}


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 09 — reference solution (the TriLog audit)")
