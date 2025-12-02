import io
import sys
import runpy


def run_program_with_input(input_str: str) -> str:
    """Helper: run 8-2.py as a script with given input and return stdout."""
    # Prepare stdin and capture stdout
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(input_str)
        sys.stdout = io.StringIO()
        # runpy.run_path executes the file as a script
        runpy.run_path("/workspaces/1202/8-2.py", run_name="__main__")
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout


def test_sample_input():
    inp = """2
5
park ABC-123
park XYZ-999
park QQQ-000
leave ABC-123
status
"""
    out = run_program_with_input(inp)
    expected = """Parked
Parked
Full
Left
Available: 1"""
    assert out == expected


def test_capacity_zero_and_leave_nonexistent():
    inp = """0
2
park AAA-111
leave AAA-111
"""
    out = run_program_with_input(inp)
    # With capacity 0, park should fail; leave should report Car not found
    assert "Full" in out
    assert "Car not found" in out


def test_double_park_same_plate():
    inp = """1
3
park A-1
park A-1
status
"""
    out = run_program_with_input(inp)
    # First park should be Parked, second should be Full (already occupied), status 0
    assert "Parked" in out.splitlines()[0]
    assert "Full" in out.splitlines()[1]
    assert out.splitlines()[-1].strip() == "Available: 0"
