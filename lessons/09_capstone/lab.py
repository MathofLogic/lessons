#!/usr/bin/env python3
"""Lesson 09 capstone lab — audit TriLog(tm) (see SPEC.md).

Implement audit() returning a dict with EXACTLY these keys:

  "laws_held"      int   — how many of the 15 laws T2's tables force
  "sacrificed"     set   — the law names that fail
  "witness"        dict  — {"law": "LEM", "at": value, "evaluates_to": value}
  "fingerprint"    str   — the pl.REGISTRY key TriLog's signature matches
  "t3"             dict  — {"tag": one of the four tags,
                            "verdict": the kernel's half_test string}
  "t4"             pl.LQ — K=42 DRAS-wrapped; scope must include the keys
                            "units" and "method" (reconstructed, honest)
  "t5"             dict  — {"correction": "decoherence",
                            "op": int (30/step under theta=100),
                            "demand": float (the shortfall at refusal)}
  "tags"           dict  — {"T1": tag, ..., "T5": tag}
  "findings_tiers" list  — the tier of each finding you made (strings)
  "composite"      str   — weakest link over your non-UNPAID tiers
  "self_note"      str   — one sentence: why the composite caps where it does
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks, close

pl = kernel()
Z, H, U = 0.0, 0.5, 1.0
V3 = (Z, H, U)

# T2's normative tables, as published:
trilog_neg = lambda a: {Z: U, U: Z, H: H}[a]
trilog_and, trilog_or, trilog_D = min, max, (U,)

TIER_ORDER = ("FORCED", "EMPIRICAL", "CONDITIONAL", "STIPULATED", "UNPAID")


def audit():
    raise NotImplementedError  # TODO: the whole capstone


# ── the grader re-derives everything ─────────────────────────────────────
_LAWS = pl.enumerate_laws(V3, trilog_neg, trilog_and, trilog_or, trilog_D)


def _decohere(step, theta):
    ctx = pl.Context(theta=theta)
    G = lambda P, ctx=None: pl.Pattern(P.v, P.L + step)
    P, op = pl.Pattern("decision", 0.0), 0
    while P.available:
        op += 1
        P = pl.propagate(P, G, ctx)
    return op, P


CHECKS = [
    ("T1 refuted by enumeration: laws_held matches the tables, not the "
     "datasheet, and is < 15",
     lambda m: m.audit()["laws_held"] == sum(_LAWS.values())
               and m.audit()["laws_held"] < 15),
    ("T1 the sacrificed set is exactly the enumerated failures",
     lambda m: set(m.audit()["sacrificed"])
               == {k for k, v in _LAWS.items() if not v}),
    ("T1 the witness is live: at the returned value, OR(a, neg(a)) "
     "evaluates as claimed and is not designated",
     lambda m: (lambda w: w["law"] == "LEM"
                and close(trilog_or(w["at"], trilog_neg(w["at"])),
                          w["evaluates_to"])
                and w["evaluates_to"] not in trilog_D)(m.audit()["witness"])),
    ("T1 fingerprint: TriLog is a registered carrier wearing a trademark",
     lambda m: m.audit()["fingerprint"] in pl.REGISTRY
               and pl.REGISTRY[m.audit()["fingerprint"]].laws == _LAWS),
    ("T3 tagged as a stipulation dressed as a property, with the kernel's "
     "reification verdict attached",
     lambda m: m.audit()["t3"]["tag"] == "stipulated"
               and m.audit()["t3"]["verdict"]
               == pl.half_test("pipeline correct", True)),
    ("T4 the bare constant is DRAS-wrapped: value 42, scope discloses "
     "units and method",
     lambda m: (lambda q: close(q.value, 42.0)
                and {"units", "method"} <= set(dict(q.scope)))
               (m.audit()["t4"])),
    ("T5 corrected: decoherence (not error), at the kernel's exact op, "
     "with the shortfall priced",
     lambda m: (lambda got, op, P: got["correction"] == "decoherence"
                and got["op"] == op
                and close(got["demand"], P.demand(100.0)))
               (m.audit()["t5"], *_decohere(30.0, 100.0))),
    ("tags: T1 refuted-as-published, T2 stipulated (tables are a "
     "convention), T4 stipulated, T5's budget claim conditional",
     lambda m: (lambda t: t["T2"] == "stipulated" and t["T4"] == "stipulated"
                and t["T1"] in ("stipulated", "forced")  # see solution note
                and t["T5"] == "conditional"
                and t["T3"] == "stipulated")(m.audit()["tags"])),
    ("composite: the weakest link over the audit's own non-UNPAID tiers, "
     "computed correctly",
     lambda m: (lambda a: a["composite"] == max(
                (t for t in a["findings_tiers"] if t != "UNPAID"),
                key=TIER_ORDER.index))(m.audit())),
    ("the audit knows its own cap: STIPULATED, and says why",
     lambda m: m.audit()["composite"] == "STIPULATED"
               and len(m.audit()["self_note"]) > 20),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 09 — capstone: the TriLog(tm) audit")
