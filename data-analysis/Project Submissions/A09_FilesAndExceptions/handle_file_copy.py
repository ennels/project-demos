#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path

print("\n------------------------------------------\n")

# Read from one .txt file and write to another while handling exceptions

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
    print("\nCopying to new file, 'backup.txt'.")
    print("Here are the contents of 'backup.txt':\n")


backup_path = Path("backup.txt")

try:
    backup_path.write_text(contents)
    
except Exception as message:
    print(f"Failed to write to '{backup_path}': {message}")

for line in backup_path.read_text().rstrip().splitlines():
    print(f"\t{line}")