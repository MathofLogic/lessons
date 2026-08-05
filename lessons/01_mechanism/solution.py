#!/usr/bin/env python3
"""Lesson 01 — reference solution. Read it AFTER attempting the lab."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab

pl = kernel()


def ex1_walltime():
    # sequence sums; the parallel block contributes only its widest branch
    return pl.L_seq([3.0, pl.L_par([9.0, 4.0, 5.0]), 7.0])   # 3+9+7 = 19


def ex2_artifact_cost():
    # redundancy is an OR: the cheapest alternative suffices
    return pl.L_or(9.0, 1.5)                                  # 1.5


def ex3_decoherence_op():
    # each op adds 45; the pattern decoheres at the first op with
    # L > 280, i.e. the smallest n with 45n > 280 -> n = 7 (L = 315)
    step, theta, n = 45.0, 280.0, 0
    L = 0.0
    while L <= theta:
        n += 1
        L += step
    return n


def ex4_shortfall():
    # demand = max(0, L - theta) at the refusal point = 315 - 280
    return 45.0 * ex3_decoherence_op() - 280.0                # 35.0


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 01 — reference solution")
