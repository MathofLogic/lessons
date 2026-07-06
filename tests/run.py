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

print("\n" + ("BUILD PASSED — the course grades what it claims to grade"
              if not fails else f"BUILD FAILED: {fails}"))
sys.exit(1 if fails else 0)
