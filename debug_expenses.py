import runpy
import sys
from pathlib import Path

workspace = Path(__file__).resolve().parent
csv_path = workspace / "Expenses.csv"
expenses_path = workspace / "expenses.py"

with csv_path.open(encoding="utf-8") as csv_file:
    sys.stdin = csv_file
    runpy.run_path(str(expenses_path), run_name="__main__")
