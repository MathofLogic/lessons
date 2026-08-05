#!/usr/bin/env python3
"""tests/run.py — the course build gate.

Three disciplines:

  1. KERNEL SEAL   the vendored pl.py must be byte-identical to the
                   sealed kernel (sha256[:16] = bfddc7d82986ba9b). The
                   course teaches against a specific, audited instrument;
                   a drifted kernel is a different course.
  2. SOLUTIONS PASS  every lesson's reference solution exits 0. A course
                   whose own answers don't hold teaches dishonesty.
  3. SKELETONS FAIL  every lesson's lab, with its TODOs untouched, exits
                   NONZERO. If the checks pass with nothing implemented,
                   the checks are vacuous and the lesson grades noise.
                   (This is the course's own falsifier.)
"""
import hashlib, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEALED = "bfddc7d82986ba9b"
fails = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(name)


print("KERNEL SEAL")
sha = hashlib.sha256((ROOT / "pl.py").read_bytes()).hexdigest()[:16]
check(f"vendored pl.py sha256[:16] == {SEALED}", sha == SEALED, sha)

lessons = sorted(p for p in (ROOT / "lessons").iterdir() if p.is_dir())
check("all nine lessons present with LESSON.md, lab.py, solution.py",
      len(lessons) == 9 and all(
          (p / "LESSON.md").exists() and (p / "lab.py").exists()
          and (p / "solution.py").exists() for p in lessons))

print("\nSOLUTIONS PASS / SKELETONS FAIL (both directions, every lesson)")
for p in lessons:
    sol = subprocess.run([sys.executable, "solution.py"], cwd=p,
                         capture_output=True, text=True, timeout=300)
    check(f"{p.name}: solution exits 0", sol.returncode == 0,
          "" if sol.returncode == 0 else
          (sol.stdout + sol.stderr).strip().splitlines()[-1][:70])
    lab = subprocess.run([sys.executable, "lab.py"], cwd=p,
                         capture_output=True, text=True, timeout=300)
    check(f"{p.name}: untouched skeleton exits NONZERO (checks are "
          f"non-vacuous)", lab.returncode != 0)


print("\nHISTORY + LEDGER (sealed grading history; claims backed by "
      "lessons_checks.py)")
import json
sys.path.insert(0, str(ROOT))
import claims as _claims
import lessons_checks as _lc

MANDIR = ROOT / "manifests"
MANDIR.mkdir(exist_ok=True)
MP = MANDIR / "lessons_manifest.json"
_prior = []
if MP.exists():
    _prior = json.loads(MP.read_text())
    check("committed grading history replays without its writer",
          _lc.replay(_prior) is True,
          "possible tampering — file preserved as evidence")
if not fails:
    _body = {"event": "grading-run", "kernel": SEALED,
             "lessons": 9, "both_directions": True}
    _last = {k: v for k, v in (_prior[-1] if _prior else {}).items()
             if k not in ("sha", "sha_prev")}
    if _last != _body and _lc.replay(_prior) in (True, None):
        prev = _prior[-1]["sha"] if _prior else "GENESIS"
        sha = hashlib.sha256((prev + json.dumps(_body, sort_keys=True))
                             .encode()).hexdigest()[:16]
        _prior.append({**_body, "sha_prev": prev, "sha": sha})
        MP.write_text(json.dumps(_prior, indent=1))

for _name, _fn in _lc.CHECKS.items():
    try:
        check(_name, _fn() is True)
    except Exception as _e:
        check(_name, False, f"{type(_e).__name__}: {_e}")
_ledgered = {c["check"] for _, cs in _claims.SECTIONS
             for c in cs if c.get("check")}
check("ledgered checks == registry (no dangling, no orphans)",
      _ledgered == set(_lc.CHECKS))

print("""
NOT claimed: that the labs teach PL — the gate proves the course
    grades what it claims to grade, nothing about what a student
    takes away.
NOT claimed: that PL is the right map — the course teaches an
    instrument and prices it; adopting it is the reader's theta.
NOT claimed: that the lesson order is forced — sequence and
    difficulty are editorial, sealed as such.""")

# ── VACUITY CANARY ────────────────────────────────────────────────────
# Regression for the defect where a carrier with an empty designated set
# scored as well as strong Kleene, because four of the five guarded laws
# passed with their guard inert. A law that holds over zero witnesses was
# never tested, and must not read as a pass.
try:
    import os as _os, sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
    from pl_witness import distinguishes as _dist
    _V = (0.0, 0.5, 1.0)
    _neg = lambda a: 1.0 - a
    _ok, _why = _dist(_V, _neg, min, max, (1.0,), [(), _V])
    print(f"  vacuity canary: degenerate carriers distinguishable : "
          f"{'yes' if _ok else 'NO — ' + _why}")
    if not _ok:
        print("  BUILD FAILED — vacuity regression")
        raise SystemExit(1)
except ImportError:
    print("  vacuity canary: pl_witness not found")
    raise SystemExit(1)

print("\n" + ("BUILD PASSED — the course grades what it claims to grade"
              if not fails else f"BUILD FAILED: {fails}"))
sys.exit(1 if fails else 0)


