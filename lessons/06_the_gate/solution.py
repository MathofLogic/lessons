#!/usr/bin/env python3
"""Lesson 06 — reference solution."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab
from lab import V3, Z, H, U, k3_neg, wk_and, wk_or

pl = kernel()


def ex1_predict_pwk():
    # Reasoning, table by table:
    # LNC: AND(1/2, neg(1/2)) = AND(1/2, 1/2) = 1/2 (infectious), and
    #      1/2 IS designated -> a contradiction lands designated -> False.
    # LEM: OR(a, neg(a)) — at a=1/2 the infectious half gives 1/2,
    #      designated; at 0 and 1 it gives 1. Designated everywhere -> True.
    # DN:  neg(neg(a)) == a for all three values -> True.
    # MP:  the designated glut no longer detaches: a=1/2 is designated and
    #      OR(neg(1/2), 0) = 1/2 designated, yet b=0 is not -> False.
    return {"LNC": False, "LEM": True, "DN": True, "MP": False}


def ex2_admit_pwk():
    return pl.register(pl.Carrier(
        "PWK  paraconsistent weak Kleene", V3, k3_neg, wk_and, wk_or,
        (H, U), ex1_predict_pwk(),
        "corrupted-but-audited records flow without explosion; "
        "detachment is the price"))


def ex3_not_closed():
    # AND as addition escapes {0,1}: 1+1 = 2 is not in V.
    return pl.Carrier("BAD  escapes V", (Z, U), lambda a: U - a,
                      lambda a, b: a + b, max, (U,), {},
                      "an operation that leaves V is a bug, not a logic")


def ex4_misdeclared():
    # K3's honest tables, dishonestly declared: LEM does not hold on
    # min/max with only 1 designated, but the author claims it does.
    return pl.Carrier("LIE  misdeclared K3", V3, k3_neg, min, max, (U,),
                      {"LEM": True},
                      "the tables are fine; the declaration is false")


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 06 — reference solution")
