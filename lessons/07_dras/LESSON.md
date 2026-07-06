# Lesson 07 — DRAS in Code: Numbers That Keep Their Receipts

*A bare number is a quantity whose history was erased. DRAS — the
De-Reification Axiom Standard — lets you erase history, and charges you
for it, on a ledger, every time.*

## The loaded quantity

```
LQ = (value, eps, L, scope, ledger)
```

- **value** — the number your dashboard wants.
- **scope** — everything the bare number silently drops: the measurement
  window, the host, the method, the baseline, the temperature. "CPU is
  73%" *of what, over what window, sampled how?* The scope is the answer,
  attached.
- **ledger** — every operation that produced this quantity, in order.
- **L** — the load: how much maintained distinction this number carries.

Combine two LQs (`*` is the AND-combination) and the machinery does what
sloppy pipelines don't: loads **add** (you now maintain both histories),
scopes **concatenate**, and the ledger records the combination. Nothing is
lost by arithmetic — only by choice.

## Reification is permitted — and priced

`reify()` is the honest version of what every metrics exporter does: it
hands you the bare float. But it also appends `REIFIED: scope erased` to
the ledger and **raises L by one distinction**. The rule is not "never
drop the scope" — dashboards need bare numbers. The rule is: *you may not
drop it for free, and you may not drop it silently.* When the incident
review asks "73% of what?", the ledger answers, including the exact moment
someone decided the question wouldn't matter.

## The 0.5 test as an instrumentation policy

Lesson 03 used the test to read documents. Here you operationalise it:
sweep your service's status page, run the test on every binary badge, and
every claim where "0.5" is coherent is a **reification in production** —
a graded quantity being served as a boolean, threshold undisclosed. Those
are precisely the quantities that should ship as LQs, scope attached,
threshold stated as the stipulation it is.

## Physical floors, temperature stated

The kernel's `landauer(bits, T)` prices irreversible erasure — and it has
no default temperature. That is deliberate: a joule figure at a hidden T
is itself a reification, and the kernel refuses to commit it. When you
price a log-retention policy in the lab, you will state 300 K out loud,
and tier the claim CONDITIONAL, because that is what it is.

## The lab

Wrap a production metric as an LQ; combine two and verify the books;
reify one and verify the charge; write the instrumentation policy that
flags every graded badge on a status page; and price a retention policy
with T explicit.
