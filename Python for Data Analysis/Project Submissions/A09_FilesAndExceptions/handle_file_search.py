#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path

print("\n------------------------------------------\n")

# Read from one .txt file and print usernames that contain a specific substring

path = Path("users.txt")

try:
    contents = path.read_text().rstrip()
  
except FileExistsError:
    print("File does not exist.")
    
except FileNotFoundError:
    print("File not found.")
    
except Exception as message:  # It's nice to not need a thousand handlers
    print(message)

else:
    print(f"Importing from '{path}':\n")
    for line in contents.splitlines():
        print(f"\t{line}")
    print("\n")
    
    # The usernames are pretty random. Might need to filter by a letter rather than a string.
    print(f"Printing all usernames from '{path}' that contain substring 's':\n")
    for line in contents.splitlines():
        if "s" in line.lower():    
            print(f"\t{line}")