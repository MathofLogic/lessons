# Lesson 03 — Analysis: Tagging Claims and the 0.5 Test

*Before you design or debug a formal system, you must read one — and most
of what a spec leans on is not written in the spec.*

## The four tags

Every load-bearing claim in a document gets exactly one tag:

- **[stipulated]** — chosen by definition or convention; could have been
  otherwise. *"The health-check timeout is 30 s."* Nothing forces 30.
- **[forced]** — follows necessarily, given the stipulations and the logic
  in force. *"Given min/max tables on {0,½,1} with D={1}, LEM fails."*
  You enumerated that in Lesson 02; no one gets to vote on it.
- **[empirical]** — asserted on measurement. *"p99 latency was 212 ms over
  the last 24 h."* It carries a scope (window, percentile method) — hold
  that thought for Lesson 07.
- **[presumed]** — inherited from a prior theory or system the document
  relies on but does not re-establish. *"TCP delivers bytes in order."*
  True, but this spec did not earn it; it imported it, along with
  everything TCP itself stipulates.

The discipline is relentless: trace every **[presumed]** back to the
**[stipulated]** it secretly rests on. That chain is the document's real
foundation, and a foundation you never name is one you cannot notice
failing.

## The 0.5 test

For any *binary* claim, ask: **what would 0.5 mean?**

- *"The deploy is safe."* Half-safe is perfectly coherent — safety is
  graded (error budgets, blast radius, rollback readiness). A binary
  carrier here is **suppressing load history**: someone chose a threshold
  and erased the choice. Verdict: reification.
- *"The feature flag is on."* Half-on is (to first order) incoherent —
  the domain may genuinely be binary. Verdict: binary may fit — *check
  the boundaries* (propagation delay is where "on" gets graded again).

The kernel ships this as `pl.half_test`, tier STIPULATED: a diagnostic
heuristic, honestly labelled as one.

## The hidden-logic question

A dashboard computes `status = probe_a AND probe_b`, coercing timeouts to
`False`. Nobody wrote "we assume classical logic" — but that coercion IS
the assumption: it forces every value into `{0,1}` so the classical tables
apply, and it does so by **fabricating an observation** (UNKNOWN → DOWN).
The honest carrier for probes-with-timeouts is K3, where the timeout stays
a value and LEM's failure at ½ is exactly the statement "you can't assert
'up or down' about a probe that never answered." Detecting silently
presumed carriers is the single highest-value analysis skill this course
teaches — production systems assume classical logic the way fish assume
water.

## The lab

A ten-claim excerpt from a fictional-but-familiar systems spec. You will
tag all ten, run the 0.5 test on the binaries, and name the presumed and
honest carriers for a coercing dashboard.
