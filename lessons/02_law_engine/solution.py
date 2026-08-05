#!/usr/bin/env python3
"""Lesson 02 — reference solution."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab

pl = kernel()


def ex1_lem(V, neg, OR, D):
    Dset = set(D)
    return all(OR(a, neg(a)) in Dset for a in V)


def ex2_lnc(V, neg, AND, D):
    Dset = set(D)
    return all(AND(a, neg(a)) not in Dset for a in V)


def ex3_headline():
    k3 = pl.REGISTRY["K3   strong Kleene"]
    l3 = pl.REGISTRY["L3   lukasiewicz"]
    return (ex1_lem(k3.V, k3.neg, k3.OR, k3.D),
            ex1_lem(l3.V, l3.neg, l3.OR, l3.D))


def ex4_signature_diff():
    k3 = pl.REGISTRY["K3   strong Kleene"]
    l3 = pl.REGISTRY["L3   lukasiewicz"]
    a = pl.enumerate_laws(k3.V, k3.neg, k3.AND, k3.OR, k3.D)
    b = pl.enumerate_laws(l3.V, l3.neg, l3.AND, l3.OR, l3.D)
    return {k for k in a if a[k] != b[k]}


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 02 — reference solution")
