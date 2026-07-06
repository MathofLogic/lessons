# Lesson 06 — Coding: Through the Gate

*Now you write against the real kernel. `register()` is where a formal
system stops being a proposal and becomes an admitted, audited carrier —
or gets refused, in public, by enumeration.*

## What the gate demands

`register(Carrier(name, V, neg, AND, OR, D, expect, note))` performs two
refusals before anything is admitted:

1. **Closure.** Every `neg(a)`, `AND(a,b)`, `OR(a,b)` must land back in
   `V`. An operation that escapes its value space is not a logic, it is a
   bug with a Greek letter. Refused, and the refusal is a FORCED claim.
2. **Declared signature.** `expect` is *your falsifiable prediction*: the
   laws you claim your tables force. The gate enumerates all 15 and
   compares. Declare LEM=True for K3's tables and you are refused — not
   because the tables are wrong, but because **you** were, and a registry
   that admits carriers whose authors misunderstand them is poisoned at
   the root. Declaration is not paperwork; it is the design discipline of
   Lesson 04 made mandatory.

Only after both does the carrier enter `pl.REGISTRY`, its enumerated law
vector attached for anyone downstream to read.

## Why this shape matters for software

This is the Admission Gate pattern, and you have already met it if you've
seen the /rigor toolbox: detectors must ship falsifiers and fixtures;
carriers must ship signatures and survive enumeration. The general form —
**a contribution states what would prove it wrong, and the system checks
before admitting** — is the single most transferable design idea in the
framework. Plugin systems, schema registries, feature-flag configs, CI
required-checks: all of them are gates, and most of them are gates that
verify nothing. You are about to build one that does.

## The carrier you will admit: PWK

Paraconsistent Weak Kleene — B3's infectious tables (`½` swallows
everything it touches) but with the middle **designated**, `D = {½, 1}`.
It models a pipeline where corrupted-but-logged records must flow (you
cannot drop them: audit requirements) without licensing everything
(explosion). You will predict its signature first, then let the gate
grade your prediction. Then you will build two carriers that *deserve*
refusal — one not closed, one mis-declared — and watch the gate do its
job on each.

```bash
python lab.py
```
