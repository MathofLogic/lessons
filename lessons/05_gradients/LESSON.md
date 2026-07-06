# Lesson 05 — Gradients and Cost Models

*A gradient is legitimate when it composes. A cost model is honest when it
distinguishes where you are from how you got there.*

## Value is a state function; load is a process function

Take a quantity that "runs" — a physical coupling with energy scale, a
config value under migrations, an exchange rate through conversions. The
kernel's Scale carrier stores it by its state variable and steps it:

```
step(E → E'):   value changes by  b·log(E'/E)        (additive rule)
                load  changes by |b·log(E'/E)|       (every step pays)
```

Two properties separate a real gradient from a hack, and the kernel
property-tests both:

1. **The group law.** Stepping `E0 → E2` directly must equal
   `E0 → E1 → E2` in **value**. If staging changes the answer, your "step"
   is not a gradient — it is two different operations wearing one name.
2. **Path dependence of load.** Walk a closed loop `E0 → … → E0` and the
   **value returns exactly** (state function — it forgets the route) but
   the **load does not** (process function — the triangle inequality on
   `|b·Δlog E|` guarantees the wandering path never undercuts the direct
   one). The value tells you where you are. The bill tells you how you
   got there.

This is the deepest debugging heuristic in the course: **systems that
track only state functions cannot explain their own costs.** A config
that migrated A→B→A is "unchanged" by diff and very much changed by bill —
ask anyone who paid for both migrations. A retried request that finally
succeeded reports the same 200 as a first-try success; the load is the
difference, and it is exactly what your latency budget was spending.

## θ makes cost models operational

A budget that nothing enforces is decoration. Attach a θ and the load
arithmetic becomes a *live* constraint: `propagate` refuses over-budget
results at exactly the op the arithmetic forces (Lesson 01), and a whole
pipeline coheres iff its `L_seq/L_par` composition fits. Capacity
planning, in this vocabulary, is choosing θ; incident review is reading
`demand()`.

## The lab

You will implement a retry gradient and have the kernel hold it to the
exact decoherence op; implement a scale-walk and verify the group law and
the closed-loop asymmetry (value returns, load doesn't) numerically; and
write the coherence check for a full pipeline under θ.
