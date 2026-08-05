#!/usr/bin/env python3
"""Lesson 07 lab — DRAS in code. Fill each TODO, then: python lab.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks, close

pl = kernel()

# ── EX 1 ─────────────────────────────────────────────────────────────────
# Wrap a p99 latency of 0.212 s as an LQ whose scope carries AT LEAST the
# keys "window", "percentile_method", and "service" (values your choice),
# with a one-entry ledger describing where it was seeded from.
def ex1_wrap_latency():
    raise NotImplementedError  # TODO: return an pl.LQ


# ── EX 2 ─────────────────────────────────────────────────────────────────
# Error budget spent = error_rate * traffic_share. Build the two LQs
# (values 0.4 and 0.6, loads 1.0 and 2.0, any scopes) and AND-combine
# them with *. Return the combined LQ. Verify for yourself before the
# grader does: what should the combined load be, and why?
def ex2_combine():
    raise NotImplementedError  # TODO: return lq_a * lq_b


# ── EX 3 ─────────────────────────────────────────────────────────────────
# Reify your EX1 quantity for the dashboard. Return the pair
# (bare_value, priced_lq) exactly as reify() hands it to you.
def ex3_reify():
    raise NotImplementedError  # TODO: return ex1_wrap_latency().reify()


# ── EX 4 ─────────────────────────────────────────────────────────────────
# The status page shows five badges. Using pl.half_test as the policy
# engine, return the sorted list of badge names that are REIFICATIONS
# (graded quantities served as booleans). The second element of each pair
# is the answer to "is 0.5 coherent here?" — your job is to supply it.
BADGES = [
    ("db_healthy", None),        # health is graded (replication lag, ...)
    ("tls_cert_valid", None),    # validity at an instant is genuinely binary
    ("deploy_safe", None),       # safety is graded
    ("feature_flag_on", None),   # on/off is binary (boundaries aside)
    ("capacity_ok", None),       # headroom is graded
]
def ex4_reified_badges():
    raise NotImplementedError  # TODO: return sorted([...]) of badge names


# ── EX 5 ─────────────────────────────────────────────────────────────────
# Price the irreversible erasure of 30 days of logs — 12 GiB — at an
# EXPLICIT 300 K, using pl.landauer(bits, T). Return the joule floor.
def ex5_retention_floor():
    raise NotImplementedError  # TODO: return joules as a float


CHECKS = [
    ("EX1 the wrapped latency carries window, method and service in scope",
     lambda m: (lambda q: close(q.value, 0.212)
                and {"window", "percentile_method", "service"}
                <= set(dict(q.scope)) and len(q.ledger) >= 1)
               (m.ex1_wrap_latency())),
    ("EX2 AND-combination: value multiplies, LOADS ADD (both histories "
     "are now maintained), ledger records the combine",
     lambda m: (lambda q: close(q.value, 0.24) and close(q.L, 3.0)
                and "AND-combine" in q.ledger)(m.ex2_combine())),
    ("EX3 reify hands back the bare float and charges one distinction",
     lambda m: (lambda bare, priced: close(bare, 0.212)
                and close(priced.L, m.ex1_wrap_latency().L + 1.0)
                and "REIFIED: scope erased" in priced.ledger)
               (*m.ex3_reify())),
    ("EX3 the original LQ is untouched (frozen): reification is a new "
     "history, not a rewrite of the old one",
     lambda m: "REIFIED: scope erased" not in m.ex1_wrap_latency().ledger),
    ("EX4 the policy flags exactly the graded badges",
     lambda m: m.ex4_reified_badges()
               == sorted(["db_healthy", "deploy_safe", "capacity_ok"])),
    ("EX4 the policy agrees with the kernel's half_test verdict strings",
     lambda m: pl.half_test("db_healthy", True).startswith("REIFICATION")
               and pl.half_test("tls_cert_valid", False).startswith("binary")),
    ("EX5 the retention floor is landauer(12 GiB in bits, 300) — T stated,"
     " never defaulted",
     lambda m: close(m.ex5_retention_floor(),
                     pl.landauer(12 * 8 * 2**30, 300), 1e-24)
               and m.ex5_retention_floor() > 0),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 07 — DRAS (you may drop the scope; not for free)")
