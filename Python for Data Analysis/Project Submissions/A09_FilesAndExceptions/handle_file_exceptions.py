#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path

print("\n------------------------------------------\n")

# Read from a .txt file and handle exceptions

path = Path("users.txt")

try:
    contents = path.read_text().rstrip()
  
except FileExistsError:
    print("File does not exist.")
    
except FileNotFoundError:
    print("File not found.")
    
except Exception:
    print("Error!")

else:
    print(f"Importing from '{path}':\n")
    for line in contents.splitlines():
        print(f"\t{line}")