#!/usr/bin/env python3
"""Lesson 07 — reference solution."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab

pl = kernel()


def ex1_wrap_latency():
    return pl.LQ(0.212, L=0.0,
                 scope=(("window", "24 h"),
                        ("percentile_method", "t-digest"),
                        ("service", "checkout")),
                 ledger=("seeded from histogram export",))


def ex2_combine():
    err = pl.LQ(0.4, L=1.0, scope=(("kind", "error_rate"),),
                ledger=("seeded",))
    share = pl.LQ(0.6, L=2.0, scope=(("kind", "traffic_share"),),
                  ledger=("seeded",))
    # AND-combination: value 0.24, load 1+2=3 (maintaining the product
    # means maintaining BOTH inputs), scopes and ledgers concatenate.
    return err * share


def ex3_reify():
    return ex1_wrap_latency().reify()


def ex4_reified_badges():
    verdicts = {
        "db_healthy": pl.half_test("db_healthy", True),
        "tls_cert_valid": pl.half_test("tls_cert_valid", False),
        "deploy_safe": pl.half_test("deploy_safe", True),
        "feature_flag_on": pl.half_test("feature_flag_on", False),
        "capacity_ok": pl.half_test("capacity_ok", True),
    }
    return sorted(k for k, v in verdicts.items()
                  if v.startswith("REIFICATION"))


def ex5_retention_floor():
    bits = 12 * 8 * 2**30            # 12 GiB in bits
    return pl.landauer(bits, 300)    # T explicit — always

if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 07 — reference solution")
