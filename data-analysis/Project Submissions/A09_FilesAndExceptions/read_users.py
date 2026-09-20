#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path


print("\n------------------------------------------\n")

# Reading and printing usernames from a .txt file

path = Path("users.txt")
contents = path.read_text().rstrip()
print(f"Importing from '{path}':\n")
for line in contents.splitlines():
    print(f"\t{line}")