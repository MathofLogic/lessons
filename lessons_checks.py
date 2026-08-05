"""
lessons_checks.py — the /lessons check registry.
==========================================================================
Named, executable checks backing the root claims.py ledger; the gate
runs every one. They force the course's grading machinery — the pinned
kernel, the non-vacuity of the labs, the sealed history — never what a
student learns from it.
"""
from __future__ import annotations
import hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent
SEALED = "bfddc7d82986ba9b"


def replay(chain):
    if not isinstance(chain, list) or not all(
            isinstance(g, dict) and "sha" in g and "sha_prev" in g
            for g in chain):
        return None
    prev = "GENESIS"
    for g in chain:
        body = {k: v for k, v in g.items()
                if k not in ("sha", "sha_prev")}
        want = hashlib.sha256((prev + json.dumps(body, sort_keys=True))
                              .encode()).hexdigest()[:16]
        if g["sha_prev"] != prev or g["sha"] != want:
            return False
        prev = g["sha"]
    return True


def chk_kernel_byte_identity():
    """The vendored kernel is the kernel: sha256(pl.py)[:16]
    recomputed from bytes equals the pinned seal — the course grades
    with the instrument it names, not a lookalike."""
    real = hashlib.sha256((ROOT / "pl.py").read_bytes()).hexdigest()[:16]
    return real == SEALED


def chk_course_is_complete():
    """Nine lessons, each with LESSON.md, lab.py, and solution.py —
    the graded surface is fully present."""
    lessons = sorted(p for p in (ROOT / "lessons").iterdir()
                     if p.is_dir())
    return len(lessons) == 9 and all(
        (p / "LESSON.md").exists() and (p / "lab.py").exists()
        and (p / "solution.py").exists() for p in lessons)


def chk_grading_is_nonvacuous():
    """Both directions on an exemplar lesson: the solution passes AND
    the untouched skeleton fails — a grader that passes everything
    grades nothing (the gate runs all nine; this check keeps the
    property named and independently executable)."""
    p = sorted(q for q in (ROOT / "lessons").iterdir()
               if q.is_dir())[0]
    sol = subprocess.run([sys.executable, "solution.py"], cwd=p,
                         capture_output=True, timeout=300)
    lab = subprocess.run([sys.executable, "lab.py"], cwd=p,
                         capture_output=True, timeout=300)
    return sol.returncode == 0 and lab.returncode != 0


def chk_history_replays():
    """The committed grading history is a sha-linked chain that
    replays by seal arithmetic alone."""
    mp = ROOT / "manifests" / "lessons_manifest.json"
    return replay(json.loads(mp.read_text())) is True


CHECKS = {
    "kernel_byte_identity": chk_kernel_byte_identity,
    "course_is_complete": chk_course_is_complete,
    "grading_is_nonvacuous": chk_grading_is_nonvacuous,
    "history_replays": chk_history_replays,
}
