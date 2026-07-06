#!/usr/bin/env python3
"""Lesson 06 lab — through the gate. Fill each TODO, then: python lab.py

You are calling the REAL kernel's register(). Its refusals print as
FORCED claims — that output is the gate working, not the lab failing.
"""
import contextlib, io, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks

pl = kernel()
Z, H, U = 0.0, 0.5, 1.0
V3 = (Z, H, U)
k3_neg = lambda a: {Z: U, U: Z, H: H}[a]
wk_and = lambda a, b: H if H in (a, b) else min(a, b)   # infectious half
wk_or = lambda a, b: H if H in (a, b) else max(a, b)


# ── EX 1 — predict PWK's signature ───────────────────────────────────────
# PWK = weak Kleene tables (wk_and / wk_or, k3_neg) with D = {1/2, 1}.
# BEFORE enumerating, predict four laws by reasoning from the tables and
# return your prediction: {"LNC": bool, "LEM": bool, "DN": bool, "MP": bool}.
# Reasoning aids: is AND(1/2, neg(1/2)) designated? is OR(a, neg(a))
# designated for EVERY a, including the infectious half? does the glut
# still detach?
def ex1_predict_pwk():
    raise NotImplementedError  # TODO: return the 4-law prediction dict


# ── EX 2 — admit PWK through the real gate ───────────────────────────────
# Build the Carrier with your EX1 prediction as its declared `expect`,
# register it with pl.register, and return the registered carrier object.
# If your prediction was wrong the gate refuses you — go back to EX1;
# that round-trip IS the lesson.
def ex2_admit_pwk():
    raise NotImplementedError  # TODO: return pl.register(pl.Carrier(...))


# ── EX 3 — build a carrier the gate must refuse: not closed ──────────────
# Return a Carrier whose AND escapes V (any V you like). Do NOT register
# it yourself; the grader will, and it expects the gate to say no.
def ex3_not_closed():
    raise NotImplementedError  # TODO: return a pl.Carrier


# ── EX 4 — build a carrier the gate must refuse: mis-declared ────────────
# Return a Carrier over V3 that IS closed, but whose declared expect
# contradicts what its tables force (e.g. claim LEM=True over K3 tables).
# Again: the grader registers it and expects refusal.
def ex4_misdeclared():
    raise NotImplementedError  # TODO: return a pl.Carrier


def _register_quietly(c):
    with contextlib.redirect_stdout(io.StringIO()):
        return pl.register(c)


CHECKS = [
    ("EX1 the prediction matches what enumeration forces on PWK's tables",
     lambda m: m.ex1_predict_pwk() == {
         k: v for k, v in pl.enumerate_laws(V3, k3_neg, wk_and, wk_or,
                                            (H, U)).items()
         if k in ("LNC", "LEM", "DN", "MP")}),
    ("EX2 PWK is admitted: it sits in the live REGISTRY with its law "
     "vector attached",
     lambda m: (lambda c: c is not None and c.name in pl.REGISTRY
                and isinstance(c.laws, dict) and len(c.laws) == 15)
               (m.ex2_admit_pwk())),
    ("EX2 the admitted signature shows the designated glut: LNC fails, "
     "LEM holds (the infectious half is designated, so a v ~a always "
     "lands designated)",
     lambda m: (lambda c: c.laws["LNC"] is False and c.laws["LEM"] is True)
               (pl.REGISTRY[m.ex2_admit_pwk().name])),
    ("EX3 the gate refuses a carrier that is not closed over V",
     lambda m: _register_quietly(m.ex3_not_closed()) is None
               and m.ex3_not_closed().name not in pl.REGISTRY),
    ("EX4 the gate refuses a closed carrier whose author mis-declared it",
     lambda m: (lambda c: _register_quietly(c) is not None
                and c.name not in pl.REGISTRY)(m.ex4_misdeclared())),
    ("EX4 the refusal was about the declaration, not the tables: the same "
     "tables with an honest declaration would enumerate fine",
     lambda m: (lambda c: sum(pl.enumerate_laws(c.V, c.neg, c.AND, c.OR,
                                                c.D).values()) > 0)
               (m.ex4_misdeclared())),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 06 — the gate (declaration is falsifiable, and checked)")
