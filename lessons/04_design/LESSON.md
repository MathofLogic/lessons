# Lesson 04 — Designing a Carrier

*Design is running up a bill on purpose. You choose `(V, G, D)` to buy the
laws your domain needs, and you state — before enumerating — what you
expect to pay.*

## The method: predict, then enumerate

An engineer designing a formal system works like an engineer designing
anything: to a spec, against a budget, with the measurement made *after*
the prediction. Concretely:

1. **Name the laws your domain needs.** Probes that time out? You need DN
   (double negation — "not not-up" should mean "up") but you must NOT
   have LEM, because asserting "up or down" about a silent probe is the
   coercion bug from Lesson 03.
2. **Choose the machinery you think buys them.** `V`, negation, AND, OR,
   designated set.
3. **Write down your expected signature.** This is the falsifiable step —
   the one that makes it design rather than doodling.
4. **Enumerate.** The law engine tells you what your tables actually
   force. Where it disagrees with your expectation, *the tables win*, and
   the disagreement is the most instructive artifact you will produce all
   day.

## Design levers, and what they cost

- **The negation at ½** is a surprisingly powerful dial. Keep `¬½ = ½`
  (K3-style) and DN holds but LEM fails. Set `¬½ = 0` (Gödel-style) and
  you get an intuitionistic flavour — DN itself becomes the sacrifice.
  One cell of one table; two different logics.
- **The AND/OR pair** is the K3-vs-Ł3 lever from Lesson 02: swap min/max
  for the Łukasiewicz pair and LEM comes back — at the price of
  idempotence, distributivity, and absorption. Ask whether your domain
  can afford `AND(a,a) ≠ a` before you buy.
- **The designated set** is the paraconsistency lever: designate the
  middle value (`D = {½,1}`, LP-style) and contradictions stop exploding —
  and detachment (MP) is the price: designated premises no longer compel
  designated conclusions.

## The frontier (inherited from the Atlas, so tagged honestly)

In the complete space of 354,294 conservative three-valued carriers —
enumerated, sealed, in /PL — **no carrier reaches 15/15**, and at the
14/15 frontier only DN or LEM can ever be the lone sacrifice. So a design
brief demanding "three values, all fifteen laws" is refused by arithmetic,
not by taste. In this course that frontier fact is **[presumed]** — we
inherit it from the Atlas's sealed run rather than re-running 7.9M checks
per lab — and Lesson 03 taught you exactly what that tag obliges us to
disclose.

## The lab

Four design briefs: build a probe carrier (DN without LEM), buy LEM back
and itemise the bill, sweep the ¬½ dial across all three settings and
tabulate what each buys, and design a paraconsistent carrier where a glut
does not detonate the database.
