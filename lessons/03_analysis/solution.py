#!/usr/bin/env python3
"""Lesson 03 — reference solution."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course import kernel, run_checks
import lab

pl = kernel()


def ex1_tags():
    return {
        "S1": "stipulated",   # three is a chosen threshold
        "S2": "forced",       # pigeonhole on 3-of-5: arithmetic compels it
        "S3": "empirical",    # a measurement, with a window
        "S4": "presumed",     # imported guarantee; not re-established here
        "S5": "stipulated",   # a setting
        "S6": "forced",       # R+W > N: follows from the stipulated levels
        "S7": "empirical",    # a dashboard reading
        "S8": "presumed",     # NTP's promise, inherited wholesale
        "S9": "stipulated",   # a chosen budget
        "S10": "stipulated",  # "fault-tolerant" is an undisclosed chosen
                              # line dressed as a property of the system
    }


def ex2_half_test():
    # "half fault-tolerant" is perfectly coherent (some faults, some
    # tolerance) -> continuous domain, binary carrier: reification.
    # "half tripped" is not, to first order -> binary may fit.
    return (pl.half_test("fault-tolerant", True),
            pl.half_test("breaker tripped", False))


def ex3_hidden_carrier():
    # coercing UNKNOWN -> 0 forces every value into {0,1}: that IS
    # assuming CL2. The probe's honest home is K3, where the timeout
    # stays a value and LEM honestly fails at it.
    return ("CL2  classical", "K3   strong Kleene")


def ex4_presumed_rests_on():
    # "exactly-once" is at-least-once delivery plus idempotent
    # processing — the queue stipulates idempotence somewhere, and this
    # spec inherited that stipulation without naming it.
    return "idempotence"


if __name__ == "__main__":
    run_checks(sys.modules[__name__], lab.CHECKS,
               "Lesson 03 — reference solution")
