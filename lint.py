#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running {' '.join(command)}:")
            print(result.stdout)
            print(result.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error running {' '.join(command)}: {str(e)}")
        return False


def main():
    # Get all Python files in the current directory
    python_files = list(Path(".").glob("**/*.py"))

    # Run black
    print("\nRunning black...")
    if not run_command(["black", "."]):
        print("Black found issues")

    # Run flake8
    print("\nRunning flake8...")
    if not run_command(["flake8", "."]):
        print("Flake8 found issues")

    # Run pylint
    print("\nRunning pylint...")
    if not run_command(["pylint", "gui.py"]):
        print("Pylint found issues")

    # Run mypy
    print("\nRunning mypy...")
    if not run_command(["mypy", "."]):
        print("Mypy found issues")


if __name__ == "__main__":
    main()
