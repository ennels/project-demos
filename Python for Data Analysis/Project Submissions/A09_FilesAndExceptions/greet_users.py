#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path
import random

print("\n------------------------------------------\n")

# Reading and printing usernames from a .txt file (with greetings)

path = Path("users.txt")
contents = path.read_text().rstrip()
print(f"Importing from '{path}' (with greetings):\n")
greetings = [
    "Hello",
    "Hi",
    "Greetings",
    "Salutations",
    "Howdy",
    "Hey there",
    "Good to see you",
    "Welcome",
    "What's up",
    "Yo"
]

for line in contents.splitlines():
    print(f"\t{random.choice(greetings)}, {line}!")