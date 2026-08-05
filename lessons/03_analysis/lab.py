#!/usr/bin/env python3
"""Lesson 03 lab — analysis. Fill each TODO, then: python lab.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from course import kernel, run_checks

pl = kernel()

# ── THE SPEC EXCERPT ─────────────────────────────────────────────────────
# Ten load-bearing claims from "OrderFlow v3 — Reliability Design".
SPEC = [
    ("S1", "A node is considered failed after three missed heartbeats."),
    ("S2", "Given the gossip tables and quorum size 3 of 5, two "
           "partitions cannot both hold quorum."),
    ("S3", "Median replication lag measured 340 ms across the fleet "
           "during the November load test."),
    ("S4", "Message delivery between services is exactly-once, as "
           "provided by the queueing layer."),
    ("S5", "We set the consistency level to QUORUM for all writes."),
    ("S6", "With QUORUM writes and QUORUM reads on 5 replicas, a read "
           "always observes the latest acknowledged write."),
    ("S7", "The p50 checkout time is 1.8 s in the current dashboard."),
    ("S8", "Clocks across the fleet are synchronised, as guaranteed by "
           "the NTP infrastructure."),
    ("S9", "The retry budget is 2 attempts per request."),
    ("S10", "The system is fault-tolerant."),
]

TAGS = ("stipulated", "forced", "empirical", "presumed")


# ── EX 1 ─────────────────────────────────────────────────────────────────
# Tag every claim. Return a dict {claim_id: tag} with tags from TAGS.
# Hints: a chosen threshold or setting is stipulated; a consequence that
# arithmetic/enumeration compels GIVEN the stipulations is forced; a
# measurement is empirical; a guarantee imported from another system this
# spec does not re-establish is presumed.
def ex1_tags():
    raise NotImplementedError  # TODO: return {"S1": "...", ..., "S10": "..."}


# ── EX 2 ─────────────────────────────────────────────────────────────────
# Run the 0.5 test on these two claims, USING pl.half_test. For each,
# first decide whether "0.5" would be a coherent value, then return the
# pair of kernel verdict strings (in this order):
#   A: "the system is fault-tolerant"     (claim S10)
#   B: "the circuit breaker is tripped"
def ex2_half_test():
    raise NotImplementedError  # TODO: return (verdict_A, verdict_B)


# ── EX 3 ─────────────────────────────────────────────────────────────────
# The OrderFlow status page computes  status = AND(probe_a, probe_b)  and
# coerces probe timeouts to 0 before evaluating. Name (a) the carrier this
# coercion silently presumes and (b) the honest carrier for probes that
# can time out — as their exact pl.REGISTRY keys.
def ex3_hidden_carrier():
    raise NotImplementedError  # TODO: return (presumed_key, honest_key)


# ── EX 4 ─────────────────────────────────────────────────────────────────
# Every [presumed] rests on someone else's [stipulated]. For claim S4
# (exactly-once delivery), return the single word naming what the queueing
# layer actually stipulates to make its guarantee hold on retries:
# choose one of: "idempotence", "ordering", "encryption", "compression".
def ex4_presumed_rests_on():
    raise NotImplementedError  # TODO: return a string


_KEY = {"S1": "stipulated", "S2": "forced", "S3": "empirical",
        "S4": "presumed", "S5": "stipulated", "S6": "forced",
        "S7": "empirical", "S8": "presumed", "S9": "stipulated",
        "S10": "stipulated"}   # S10: an undisclosed threshold dressed
                               # as a property — a chosen line, unstated

CHECKS = [
    ("EX1 all ten tags are legal tag names",
     lambda m: set(m.ex1_tags()) == set(_KEY)
               and all(t in TAGS for t in m.ex1_tags().values())),
    ("EX1 at least 8/10 tags match the answer key (tagging is a skill, "
     "not a lottery)",
     lambda m: sum(m.ex1_tags()[k] == v for k, v in _KEY.items()) >= 8),
    ("EX1 the two guarantees imported from other systems are both presumed",
     lambda m: m.ex1_tags()["S4"] == "presumed"
               and m.ex1_tags()["S8"] == "presumed"),
    ("EX2 'fault-tolerant' is a reification; 'breaker tripped' may be "
     "binary — verdicts are the kernel's own strings",
     lambda m: m.ex2_half_test()
               == (pl.half_test("fault-tolerant", True),
                   pl.half_test("breaker tripped", False))),
    ("EX3 coercion presumes CL2; the honest probe carrier is K3",
     lambda m: m.ex3_hidden_carrier()
               == ("CL2  classical", "K3   strong Kleene")
               and all(k in pl.REGISTRY for k in m.ex3_hidden_carrier())),
    ("EX4 exactly-once rests on stipulated idempotence",
     lambda m: m.ex4_presumed_rests_on().strip().lower() == "idempotence"),
]

if __name__ == "__main__":
    run_checks(sys.modules[__name__], CHECKS,
               "Lesson 03 — analysis (tag the load before you trust it)")
