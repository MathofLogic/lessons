#!/usr/bin/env python3
"""Lesson 08 lab — debugging formal systems. Fill each TODO, then run."""
import hashlib, json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks, close

pl = kernel()
Z, H, U = 0.0, 0.5, 1.0
V3 = (Z, H, U)

# ── EX 1 — the fuzzy LEM witness ─────────────────────────────────────────
# Fuzzy: neg = 1-x, OR = max. Return the x in [0,1] at which LEM fails
# MAXIMALLY (where OR(x, neg(x)) is furthest below 1).
def ex1_fuzzy_lem_witness():
    raise NotImplementedError  # TODO: return a float


# ── EX 2 — the probability distributivity witness ────────────────────────
# PROB: AND = a*b, OR = a+b-a*b (independence stipulated). Return a
# triple (a, b, c) witnessing  a AND (b OR c)  !=  (a AND b) OR (a AND c),
# plus the two differing values: ((a,b,c), lhs, rhs).
def ex2_prob_distrib_witness():
    raise NotImplementedError  # TODO: return ((a, b, c), lhs, rhs)


# ── EX 3 — fingerprint the mysteries ─────────────────────────────────────
# Three mystery systems, tables only. Identify each by differential
# enumeration against pl.REGISTRY and return
#   {"NULLISH": key, "VENDOR_TRIBOOL": key, "LEGACY_RULES": key}
# where key is the exact pl.REGISTRY key whose 15-law signature matches.
#
# NULLISH is SQL NULL semantics: NOT NULL = NULL; AND is falsity-
# dominant (FALSE beats NULL); OR is truth-dominant (TRUE beats NULL).
MYSTERIES = {
    "NULLISH": (lambda a: {Z: U, U: Z, H: H}[a], min, max, (U,)),
    "VENDOR_TRIBOOL": (lambda a: {Z: U, U: Z, H: H}[a],
                       lambda a, b: H if H in (a, b) else min(a, b),
                       lambda a, b: H if H in (a, b) else max(a, b), (U,)),
    "LEGACY_RULES": (lambda a: {Z: U, U: Z, H: Z}[a], min, max, (U,)),
}
def ex3_fingerprint():
    raise NotImplementedError  # TODO: return the mapping dict


# ── EX 4 — locate the tamper ─────────────────────────────────────────────
# A sealed chain: each generation carries sha_prev and sha, where
# sha = sha256(prev_sha + json(body, sort_keys=True))[:16] and body is the
# generation without its two sha fields. Return the index of the FIRST
# generation at which replay breaks, or None if the chain is intact.
# (pl.replay tells you IF a chain is intact; your job is WHERE it isn't.)
def ex4_locate_tamper(chain):
    raise NotImplementedError  # TODO: return int index or None


# ── fixtures for EX 4 ────────────────────────────────────────────────────
def _mkchain(n=6):
    ch = []
    for i in range(n):
        body = {"gen": i, "event": f"deploy-{i}", "ok": True}
        prev = ch[-1]["sha"] if ch else "GENESIS"
        sha = hashlib.sha256((prev + json.dumps(body, sort_keys=True))
                             .encode()).hexdigest()[:16]
        ch.append({**body, "sha_prev": prev, "sha": sha})
    return ch


def _tampered(idx):
    ch = json.loads(json.dumps(_mkchain()))
    ch[idx]["ok"] = False           # the forged generation
    return ch


def _sig(quad):
    neg, AND, OR, D = quad
    return pl.enumerate_laws(V3, neg, AND, OR, D)


CHECKS = [
    ("EX1 the witness kills fuzzy LEM (OR(x, 1-x) < 1) at its deepest "
     "point (0.5, the unique maximal witness)",
     lambda m: close(m.ex1_fuzzy_lem_witness(), 0.5)
               and max(m.ex1_fuzzy_lem_witness(),
                       1 - m.ex1_fuzzy_lem_witness()) < 1.0),
    ("EX2 the witness is real: lhs and rhs computed by the PROB rules "
     "genuinely differ at the returned triple",
     lambda m: (lambda t, lhs, rhs:
                (lambda a, b, c:
                 close(lhs, a * (b + c - b * c)) and
                 close(rhs, (a * b) + (a * c) - (a * b) * (a * c)) and
                 abs(lhs - rhs) > 1e-9)(*t))(*m.ex2_prob_distrib_witness())),
    ("EX3 NULLISH fingerprints as strong Kleene — SQL has been running "
     "K3 since 1986",
     lambda m: m.ex3_fingerprint()["NULLISH"] == "K3   strong Kleene"
               and _sig(MYSTERIES["NULLISH"])
               == pl.REGISTRY["K3   strong Kleene"].laws),
    ("EX3 the other two fingerprint by signature match (weak Kleene's "
     "infectious half; Goedel's DN sacrifice)",
     lambda m: m.ex3_fingerprint()["VENDOR_TRIBOOL"] == "B3   weak Kleene"
               and m.ex3_fingerprint()["LEGACY_RULES"] == "G3   goedel"),
    ("EX4 an intact chain locates no tamper",
     lambda m: m.ex4_locate_tamper(_mkchain()) is None
               and pl.replay(_mkchain())),
    ("EX4 the tamper is located AT ITS LINK, for every position",
     lambda m: all(m.ex4_locate_tamper(_tampered(i)) == i
                   for i in range(6))),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 08 — debugging (witness, fingerprint, localise)")
