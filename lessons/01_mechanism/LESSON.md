# Lesson 01 — The Mechanism: `P / G → Q`

*Analysis begins with one operator. Everything later — carriers, laws,
audits — is a parameter setting of what you learn here.*

## The three objects

```
P / G → Q      inside a context  C = (θ, T)
```

- **P = (v, L)** — a *loaded pattern*. `v` is a value in some value space
  `V`; `L ≥ 0` is the **load**: the accumulated cost of producing and
  maintaining that value. `L = 0` is the seed state — no history, no bill.
- **G** — a *gradient*: a function `Pattern → Pattern`. It decomposes into
  a value rule (what happens to `v`) and a load rule (what it costs).
- **C = (θ, T)** — the *context*. `θ` is the coherence threshold: how much
  load this context can absorb. `T` is a temperature, required whenever a
  cost is quoted in joules (a bare energy constant at a hidden temperature
  is a smuggled assumption — you will meet this again in Lesson 07).

`propagate(P, G, ctx)` applies the gradient and then does the one thing
most frameworks skip: it **checks the bill**. If `Q.L > θ`, the result
*decoheres* — it comes back flagged `available=False`, tagged
`decoherent`, unusable downstream. Read that carefully: decoherence is
**not an error**. Nothing went wrong. The context simply cannot afford the
result, and the kernel refuses to pretend otherwise. A timeout, a blown
latency budget, an out-of-memory kill — these are decoherences your
systems already perform; the kernel makes the arithmetic explicit.

## The load rules (the cost model, stipulated and then verified)

| operation | load rule | systems reading |
|---|---|---|
| AND | `L(P∧Q) = L(P) + L(Q)` | maintain both at once — costs add |
| OR | `L(P∨Q) = min(L(P), L(Q))` | the cheapest alternative suffices |
| sequence | `Σ Lᵢ` | one worldline pays every step |
| parallel | `max Lᵢ` | walltime of the widest branch |

If those look familiar, they should: **your CI pipeline's walltime is this
arithmetic.** Sequence sums, parallel maxes, a cache is an OR. (This
accounting — AND=+, OR=min on `[0,∞)` — is the tropical semiring, and the
kernel registers its own cost model as a carrier and audits it. The
auditor's books are on the books.)

Two useful pattern methods: `P.coheres(θ)` asks whether the bill fits;
`P.demand(θ)` prices the shortfall — `max(0, L − θ)` — which is what you
report when a budget blows: not "failed", but "over by this much".

## What the lab asks of you

Four exercises, graded against the kernel's own machinery: compute a
pipeline's walltime with the load rules, price a redundant alternative,
predict the exact operation at which a chained gradient decoheres under a
θ, and price a shortfall. Predictions are checked by *running* the kernel
— the ground truth is propagated, not looked up.

```bash
python lab.py        # grade your work (skeleton fails honestly)
python solution.py   # the reference, if you're stuck — read it last
```
