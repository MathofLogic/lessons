#!/usr/bin/env python3
"""Lesson 04 — reference solution."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab

pl = kernel()
Z, H, U = 0.0, 0.5, 1.0
V3 = (Z, H, U)

k3_neg = lambda a: {Z: U, U: Z, H: H}[a]
luk_and = lambda a, b: max(0.0, a + b - 1.0)
luk_or = lambda a, b: min(1.0, a + b)


def ex1_probe_carrier():
    # K3: neg fixes the unknown, min/max, only full truth designated.
    # DN holds (neg(neg(a)) == a everywhere); LEM fails at the unknown.
    return (k3_neg, min, max, (U,))


def ex2_buy_lem():
    # Same V, same neg — swap the gradient for the Lukasiewicz pair.
    # LEM returns: OR(1/2, 1/2) = min(1, 1) = 1. The bill, recomputed
    # from the tables: idempotence (both), distributivity, absorption.
    quad = (k3_neg, luk_and, luk_or, (U,))
    a = pl.enumerate_laws(V3, *ex1_probe_carrier())
    b = pl.enumerate_laws(V3, *quad)
    bill = {k for k in a if a[k] and not b[k]}
    return quad, bill


def ex3_sweep():
    out = {}
    for h in (Z, H, U):
        neg = lambda a, h=h: {Z: U, U: Z, H: h}[a]
        L = pl.enumerate_laws(V3, neg, min, max, (U,))
        out[h] = (L["LEM"], L["DN"])
    return out
    # 0.0 -> Goedel flavour: DN is the sacrifice
    # 0.5 -> K3: DN holds, LEM fails
    # 1.0 -> dual flavour: enumeration decides; the dial is one cell


def ex4_paraconsistent():
    # LP: designate the glut. LNC fails BY DESIGN (the glut is both
    # asserted and denied, and asserted still), min/max keep
    # commutativity, and the price is detachment: MP fails, because a
    # designated glut premise no longer compels a designated conclusion.
    return (k3_neg, min, max, (H, U)), "MP"


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 04 — reference solution")
