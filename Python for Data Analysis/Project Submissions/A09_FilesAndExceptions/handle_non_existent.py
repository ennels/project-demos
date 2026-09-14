#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path

print("\n\n------------------------------------------\n")

# Section 1 - Handling a File That Doesn't Exist

path = Path("non_existent.txt")

try:
    print(path.read_text())

except FileNotFoundError:
    print(f"File '{path}' not found.")