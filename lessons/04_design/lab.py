#!/usr/bin/env python3
"""Lesson 04 lab — designing carriers. Fill each TODO, then: python lab.py

Every exercise returns machinery, and the grader ENUMERATES it. Your
design is judged by what your tables force, not by what you meant.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks

pl = kernel()
Z, H, U = 0.0, 0.5, 1.0
V3 = (Z, H, U)


# ── EX 1 — the probe carrier ─────────────────────────────────────────────
# Design brief: three values (down / unknown / up), and the enumerated
# signature must have DN=True and LEM=False (Lesson 03's honest probe
# logic). Return (neg, AND, OR, D).
def ex1_probe_carrier():
    raise NotImplementedError  # TODO: return (neg, AND, OR, D)


# ── EX 2 — buy LEM back, itemise the bill ────────────────────────────────
# Design brief: same V3, same negation as EX1, but LEM must ENUMERATE to
# True. Return ((neg, AND, OR, D), bill) where bill is the set of law
# names that your design pays (holds in EX1's carrier but fails in this
# one). The grader recomputes the bill from your tables.
def ex2_buy_lem():
    raise NotImplementedError  # TODO: return ((neg, AND, OR, D), set)


# ── EX 3 — sweep the negation dial ───────────────────────────────────────
# Fix AND=min, OR=max, D={1}. Sweep neg(1/2) over {0, 1/2, 1} (negation
# stays conservative: neg(0)=1, neg(1)=0). Return a dict
#   {setting: (LEM, DN)}  for setting in (0.0, 0.5, 1.0)
# computed by ENUMERATION on each resulting carrier.
def ex3_sweep():
    raise NotImplementedError  # TODO: return {0.0: (b,b), 0.5: (b,b), 1.0: (b,b)}


# ── EX 4 — the paraconsistent brief ──────────────────────────────────────
# Design brief: a migration reconciler holds BOTH "row present" and "row
# absent" from two half-migrated shards. Under CL2 this glut designates
# everything (explosion). Design a 3-valued carrier where a glut can be
# designated without explosion: the enumerated signature must have
# LNC=False (the glut is designated) while AND/OR stay commutative.
# State the price: also return the law you expect to lose for it.
# Return ((neg, AND, OR, D), price_law_name).
def ex4_paraconsistent():
    raise NotImplementedError  # TODO: return ((neg, AND, OR, D), "LAW")


def _laws(m, quad):
    neg, AND, OR, D = quad
    return pl.enumerate_laws(V3, neg, AND, OR, D)


CHECKS = [
    ("EX1 enumerates to DN=True, LEM=False (the probe signature)",
     lambda m: (lambda L: L["DN"] and not L["LEM"])(_laws(m, m.ex1_probe_carrier()))),
    ("EX1 the carrier is closed over V (the gate's first demand)",
     lambda m: (lambda q: all(q[0](a) in V3 for a in V3) and
                all(q[1](a, b) in V3 and q[2](a, b) in V3
                    for a in V3 for b in V3))(m.ex1_probe_carrier())),
    ("EX2 LEM enumerates to True in the redesign",
     lambda m: _laws(m, m.ex2_buy_lem()[0])["LEM"]),
    ("EX2 the itemised bill is exactly the laws the redesign pays",
     lambda m: (lambda a, b, bill:
                bill == {k for k in a if a[k] and not b[k]} and len(bill) >= 3)
        (_laws(m, m.ex1_probe_carrier()), _laws(m, m.ex2_buy_lem()[0]),
         set(m.ex2_buy_lem()[1]))),
    ("EX3 the sweep matches enumeration at every dial setting",
     lambda m: all(
        m.ex3_sweep()[h] == (lambda L: (L["LEM"], L["DN"]))(
            pl.enumerate_laws(V3, (lambda a, h=h: {Z: U, U: Z, H: h}[a]),
                              min, max, (U,)))
        for h in (Z, H, U))),
    ("EX3 the dial is real: settings do not all force the same (LEM, DN)",
     lambda m: len(set(m.ex3_sweep().values())) >= 2),
    ("EX4 the glut is designated without explosion: LNC=False, comm holds",
     lambda m: (lambda L: not L["LNC"] and L["ANDcomm"] and L["ORcomm"])
               (_laws(m, m.ex4_paraconsistent()[0]))),
    ("EX4 the declared price is real: that law enumerates to False",
     lambda m: _laws(m, m.ex4_paraconsistent()[0])[m.ex4_paraconsistent()[1]]
               is False),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 04 — design (the tables win; check the receipt)")
