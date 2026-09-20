#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path

print("\n------------------------------------------\n")

# Reading and counting usernames within a .txt file

path = Path("users.txt")
contents = path.read_text().rstrip()
print(f"Usernames stored in '{path}': {len(contents.splitlines())}\n")