#!/usr/bin/env python3
"""Lesson 02 lab — the law engine. Fill each TODO, then: python lab.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks

pl = kernel()

# ── EX 1 ─────────────────────────────────────────────────────────────────
# Write LEM as an enumeration: given (V, neg, OR, D), return True iff
# OR(a, neg(a)) is designated for EVERY a in V. No special cases.
def ex1_lem(V, neg, OR, D):
    raise NotImplementedError  # TODO


# ── EX 2 ─────────────────────────────────────────────────────────────────
# Write LNC the same way: True iff AND(a, neg(a)) is NOT designated for
# every a in V.
def ex2_lnc(V, neg, AND, D):
    raise NotImplementedError  # TODO


# ── EX 3 ─────────────────────────────────────────────────────────────────
# Reproduce the headline with YOUR enumerator from EX1: return the pair
# (lem_in_K3, lem_in_L3) — booleans — using the carriers from pl.REGISTRY
# ("K3   strong Kleene" and "L3   lukasiewicz").
def ex3_headline():
    raise NotImplementedError  # TODO: return (bool, bool)


# ── EX 4 ─────────────────────────────────────────────────────────────────
# Two carriers' full signatures can be compared law by law. Using
# pl.enumerate_laws on the K3 and L3 carriers, return the SET of law
# names on which they disagree.
def ex4_signature_diff():
    raise NotImplementedError  # TODO: return a set of law-name strings


def _agree_with_kernel(m, mine, kern_key):
    for c in pl.REGISTRY.values():
        args = ((c.V, c.neg, c.OR, c.D) if kern_key == "LEM"
                else (c.V, c.neg, c.AND, c.D))
        if mine(*args) != c.laws[kern_key]:
            return False
    return True


CHECKS = [
    ("EX1 your LEM enumerator agrees with the kernel on all 7 carriers",
     lambda m: _agree_with_kernel(m, m.ex1_lem, "LEM")),
    ("EX2 your LNC enumerator agrees with the kernel on all 7 carriers",
     lambda m: _agree_with_kernel(m, m.ex2_lnc, "LNC")),
    ("EX3 headline: same V, LEM fails in K3 and is forced in L3",
     lambda m: m.ex3_headline() == (False, True)),
    ("EX4 diff includes LEM (the famous one) and matches the enumeration",
     lambda m: (lambda got, want: got == want and "LEM" in got)
        (set(m.ex4_signature_diff()),
         {k for k in pl.REGISTRY["K3   strong Kleene"].laws
          if pl.REGISTRY["K3   strong Kleene"].laws[k]
          != pl.REGISTRY["L3   lukasiewicz"].laws[k]})),
    ("EX4 the diff is a real price list: L3 buys LEM by paying elsewhere",
     lambda m: len(m.ex4_signature_diff()) >= 3),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 02 — the law engine (laws are enumerated, not cited)")
