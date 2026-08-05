"""
course.py — the shared harness of the PL lessons.
==========================================================================
Two jobs, nothing else:

  kernel()      boot the vendored reference kernel (pl.py) through its own
                full self-audit, in a scratch working directory, and hand
                back the live module — ONLY if it earned exit 0. Cached
                per process. A kernel that failed its enumeration teaches
                nobody anything; the course refuses to run on one.

  run_checks()  the grader every lab and solution shares. Each check is a
                (name, fn) pair; fn receives the module under grade and
                returns truthiness. Exceptions are failures with the
                reason attached — an exercise you haven't done yet fails
                honestly (NotImplementedError), it doesn't crash the lab.

The same grader grades the skeleton and the solution. That is the course's
build discipline: a lab skeleton MUST fail (if the checks pass with the
TODOs still in place, the checks are vacuous) and a solution MUST pass.
tests/run.py enforces both directions for every lesson.
"""
import contextlib, importlib.util, io, os, pathlib, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent
_PL = None


def kernel(verbose=False):
    """Boot pl.py on a passing self-audit; cached per process."""
    global _PL
    if _PL is not None:
        return _PL
    spec = importlib.util.spec_from_file_location("pl", ROOT / "pl.py")
    mod = importlib.util.module_from_spec(spec)
    here, code = os.getcwd(), None
    with tempfile.TemporaryDirectory() as scratch:
        os.chdir(scratch)
        try:
            with contextlib.redirect_stdout(
                    sys.stdout if verbose else io.StringIO()):
                spec.loader.exec_module(mod)
            code = 0
        except SystemExit as e:
            code = e.code or 0
        finally:
            os.chdir(here)
    if code != 0 or getattr(mod, "FAILED", None):
        raise RuntimeError("kernel self-audit FAILED — course refuses to run")
    _PL = mod
    return mod


def run_checks(module, checks, title=""):
    """Grade `module` against `checks`; print a manifest; exit honestly."""
    if title:
        print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")
    fails = []
    for name, fn in checks:
        try:
            ok, why = bool(fn(module)), ""
        except NotImplementedError:
            ok, why = False, "  (not implemented yet — that's your exercise)"
        except Exception as e:
            ok, why = False, f"  ({type(e).__name__}: {str(e)[:50]})"
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{why}")
        if not ok:
            fails.append(name)
    n = len(checks)
    print(f"\n  {n - len(fails)}/{n} checks held."
          + ("  Lesson complete — check the receipt." if not fails else
             "  Keep going: a FAIL names exactly what is still owed."))
    sys.exit(1 if fails else 0)


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol
