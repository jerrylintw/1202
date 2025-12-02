import io
import sys
import runpy


def run_program(input_str: str) -> str:
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(input_str)
        sys.stdout = io.StringIO()
        runpy.run_path('/workspaces/1202/8-3.py', run_name='__main__')
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout


def test_8_3_sample():
    inp = """2
5
park ABC-123
park XYZ-999
park QQQ-000
leave ABC-123
status
"""
    out = run_program(inp)
    expected = """Parked
Parked
Full
Left
Available: 1"""
    assert out == expected


def test_8_3_zero_capacity_and_not_found():
    inp = """0
2
park AAA-111
leave AAA-111
"""
    out = run_program(inp)
    assert "Full" in out
    assert "Car not found" in out


def test_8_3_double_park():
    inp = """1
3
park A-1
park A-1
status
"""
    out = run_program(inp)
    lines = out.splitlines()
    assert lines[0].strip() == "Parked"
    assert lines[1].strip() == "Full"
    assert lines[2].strip() == "Available: 0"
