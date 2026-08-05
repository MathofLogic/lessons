#!/usr/bin/env python3
"""Lesson 01 lab — the mechanism. Fill each TODO, then: python lab.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks, close

pl = kernel()

# ── EX 1 ─────────────────────────────────────────────────────────────────
# A deploy pipeline:  fetch(3) -> [ compile(9) || lint(4) || docs(5) ] ->
# test(7). Compute its walltime using ONLY pl.L_seq and pl.L_par.
def ex1_walltime():
    raise NotImplementedError  # TODO: return the walltime as a float


# ── EX 2 ─────────────────────────────────────────────────────────────────
# The same artifact can be rebuilt (load 9.0) or pulled from a warm cache
# (load 1.5). What does maintaining "the artifact is available" cost?
# Use the OR load rule from the kernel.
def ex2_artifact_cost():
    raise NotImplementedError  # TODO: return the load as a float


# ── EX 3 ─────────────────────────────────────────────────────────────────
# A request handler retries; each retry is a gradient step adding 45 ms of
# load. The latency budget is theta = 280 ms. WITHOUT running propagate,
# predict the FIRST op number (1-based) at which the pattern decoheres.
# The grader will run the kernel and hold you to the exact op.
def ex3_decoherence_op():
    raise NotImplementedError  # TODO: return an int


# ── EX 4 ─────────────────────────────────────────────────────────────────
# At the moment of decoherence in EX 3, what shortfall does the pattern
# report? (This is Pattern.demand(theta): the amount the budget is over
# by — the honest number to put in the incident report.)
def ex4_shortfall():
    raise NotImplementedError  # TODO: return the demand as a float


# ── ground truth is PROPAGATED, never looked up ─────────────────────────
def _kernel_decoherence(step, theta):
    ctx = pl.Context(theta=theta)
    G = lambda P, ctx=None: pl.Pattern(P.v, P.L + step)
    P, op = pl.Pattern("rq", 0.0), 0
    while P.available:
        op += 1
        P = pl.propagate(P, G, ctx)
    return op, P


CHECKS = [
    ("EX1 walltime equals the kernel's L_seq/L_par on the same DAG",
     lambda m: close(m.ex1_walltime(),
                     pl.L_seq([3.0, pl.L_par([9.0, 4.0, 5.0]), 7.0]))),
    ("EX1 sanity: parallel maxes — the answer is not 3+9+4+5+7",
     lambda m: not close(m.ex1_walltime(), 28.0)),
    ("EX2 a redundant alternative costs the min (the OR rule)",
     lambda m: close(m.ex2_artifact_cost(), pl.L_or(9.0, 1.5))),
    ("EX3 predicted op matches the op the kernel actually decoheres at",
     lambda m: m.ex3_decoherence_op() == _kernel_decoherence(45.0, 280.0)[0]),
    ("EX3 the decohered pattern is flagged and tagged, not erroring",
     lambda m: (lambda P: P.available is False and "decoherent" in P.tags)
               (_kernel_decoherence(45.0, 280.0)[1])),
    ("EX4 shortfall equals Pattern.demand(theta) at the decoherence point",
     lambda m: close(m.ex4_shortfall(),
                     _kernel_decoherence(45.0, 280.0)[1].demand(280.0))),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 01 — the mechanism (graded against the live kernel)")
