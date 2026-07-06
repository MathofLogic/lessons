#!/usr/bin/env python3
"""Lesson 05 lab — gradients and cost models. Fill each TODO, then run."""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks, close

pl = kernel()


# ── EX 1 — a gradient the kernel can drive ───────────────────────────────
# Write a retry gradient: G(P, ctx=None) returns a NEW Pattern with the
# same value and load increased by exactly 60.0. (Patterns are frozen —
# construct, don't mutate.)
def ex1_retry_gradient():
    raise NotImplementedError  # TODO: return the gradient function G


# ── EX 2 — the group law ─────────────────────────────────────────────────
# A running quantity stored by its inverse: inv' = inv - b*log(E'/E).
# Implement step(inv, E, E2, b) -> (new_inv, load_paid) with
# load_paid = abs(b*log(E2/E)).
def ex2_step(inv, E, E2, b):
    raise NotImplementedError  # TODO: return (new_inv, load_paid)


# ── EX 3 — the closed loop ───────────────────────────────────────────────
# Walk the loop E0 -> E1 -> E2 -> E0 with your ex2_step (b fixed).
# Return (value_drift, total_load): the absolute difference between the
# starting and ending inv, and the summed load of the three legs.
# Prediction to verify: drift ~ 0 (state function), load > 0 (process
# function) and load >= the direct-path load of any single leg.
def ex3_closed_loop(inv0=137.036, E0=0.511, E1=91.188, E2=1000.0, b=0.67):
    raise NotImplementedError  # TODO: return (value_drift, total_load)


# ── EX 4 — coherence of a pipeline under theta ───────────────────────────
# stages: a list where each element is either a float (sequential stage)
# or a list of floats (a parallel block). Return True iff the composed
# load L_seq(...) fits within theta. Use pl.L_seq / pl.L_par.
def ex4_coheres(stages, theta):
    raise NotImplementedError  # TODO: return bool


def _drive(m):
    G = m.ex1_retry_gradient()
    ctx = pl.Context(theta=250.0)
    P, op = pl.Pattern("rq", 0.0), 0
    while P.available:
        op += 1
        P = pl.propagate(P, G, ctx)
    return op, P


CHECKS = [
    ("EX1 the kernel drives your gradient to decoherence at op 5 "
     "(60*5=300 > 250), flagged and tagged",
     lambda m: (lambda op, P: op == 5 and not P.available
                and "decoherent" in P.tags and close(P.L, 300.0))(*_drive(m))),
    ("EX1 the gradient constructs (frozen patterns are never mutated)",
     lambda m: (lambda P, Q: P.L == 0.0 and close(Q.L, 60.0) and Q is not P)
               (pl.Pattern("x", 0.0),
                m.ex1_retry_gradient()(pl.Pattern("x", 0.0)))),
    ("EX2 the group law: E0->E2 direct equals E0->E1->E2 staged, in value",
     lambda m: (lambda direct, mid: close(direct,
                m.ex2_step(mid, 91.188, 1000.0, 0.67)[0], 1e-9))
               (m.ex2_step(137.036, 0.511, 1000.0, 0.67)[0],
                m.ex2_step(137.036, 0.511, 91.188, 0.67)[0])),
    ("EX2 every step pays: load is |b*dlogE|, never negative",
     lambda m: close(m.ex2_step(10.0, 1.0, math.e, 2.0)[1], 2.0)
               and m.ex2_step(10.0, math.e, 1.0, 2.0)[1] > 0),
    ("EX3 the loop closes in value (drift < 1e-9): a state function "
     "forgets the route",
     lambda m: m.ex3_closed_loop()[0] < 1e-9),
    ("EX3 the loop does NOT close in load: the bill remembers the route",
     lambda m: (lambda drift, load: load > 0 and
                load >= abs(0.67 * math.log(91.188 / 0.511)))
               (*m.ex3_closed_loop())),
    ("EX4 a pipeline coheres exactly when its composed load fits theta",
     lambda m: m.ex4_coheres([3.0, [9.0, 4.0, 5.0], 7.0], 19.0) is True
               and m.ex4_coheres([3.0, [9.0, 4.0, 5.0], 7.0], 18.9) is False
               and m.ex4_coheres([2.0, [8.0, 8.0], 2.0], 12.0) is True),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 05 — gradients compose; bills remember")
