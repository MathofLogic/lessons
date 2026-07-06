#!/usr/bin/env python3
"""Lesson 08 — reference solution."""
import hashlib, json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab
from lab import MYSTERIES, V3

pl = kernel()


def ex1_fuzzy_lem_witness():
    # OR(x, 1-x) = max(x, 1-x), minimised where the two arms meet: 0.5.
    # There LEM's "always designated" bottoms out at 0.5 — one point,
    # law dead, and this point is the deepest failure.
    return 0.5


def ex2_prob_distrib_witness():
    a = b = c = 0.5
    lhs = a * (b + c - b * c)                       # a AND (b OR c) = 0.375
    ab, ac = a * b, a * c
    rhs = ab + ac - ab * ac                         # (a^b) v (a^c) = 0.4375
    return (a, b, c), lhs, rhs
    # The refactor "distribute the AND over the OR" changes the number.
    # Boolean-algebra rewrites are NOT sound on the probability carrier.


def ex3_fingerprint():
    out = {}
    for name, quad in MYSTERIES.items():
        neg, AND, OR, D = quad
        sig = pl.enumerate_laws(V3, neg, AND, OR, D)
        matches = [k for k, c in pl.REGISTRY.items() if c.laws == sig]
        out[name] = matches[0]      # the signature narrows to a class;
    return out                      # here each class has one registered rep


def ex4_locate_tamper(chain):
    prev = "GENESIS"
    for i, g in enumerate(chain):
        body = {k: v for k, v in g.items() if k not in ("sha", "sha_prev")}
        want = hashlib.sha256((prev + json.dumps(body, sort_keys=True))
                              .encode()).hexdigest()[:16]
        if g["sha_prev"] != prev or g["sha"] != want:
            return i                # trust ends exactly here
        prev = g["sha"]
    return None


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 08 — reference solution")
