#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path

print("\n------------------------------------------\n")

# Reading usernames (and printing their lengths) from within a .txt file

path = Path("users.txt")
contents = path.read_text().rstrip().splitlines()
print(f"Importing from '{path}':\n")
print("\n\tUSERNAMES\t\t\tLENGTHS\n")

for line in contents:
    print(f"\t{line}\t\t\t{len(line)}")