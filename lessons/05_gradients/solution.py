#!/usr/bin/env python3
"""Lesson 05 — reference solution."""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab

pl = kernel()


def ex1_retry_gradient():
    # construct a new Pattern; frozen dataclasses forbid mutation, and
    # that prohibition IS the accounting: history accumulates, always.
    return lambda P, ctx=None: pl.Pattern(P.v, P.L + 60.0)


def ex2_step(inv, E, E2, b):
    d = b * math.log(E2 / E)
    return inv - d, abs(d)     # value rule additive; load rule pays |d|


def ex3_closed_loop(inv0=137.036, E0=0.511, E1=91.188, E2=1000.0, b=0.67):
    inv, load = inv0, 0.0
    for a, c in ((E0, E1), (E1, E2), (E2, E0)):
        inv, paid = ex2_step(inv, a, c, b)
        load += paid
    return abs(inv - inv0), load
    # drift ~ 0: the log-deltas telescope to zero around any loop.
    # load > 0: absolute values do not telescope. Where you are is not
    # how you got there.


def ex4_coheres(stages, theta):
    legs = [pl.L_par(s) if isinstance(s, list) else float(s) for s in stages]
    return pl.L_seq(legs) <= theta


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 05 — reference solution")
