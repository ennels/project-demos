#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path

print("\n------------------------------------------\n")

# Writing usernames to a .txt file

usernames = ['caninepecans',
             'idiopathicblackberries',
             'jerboatrout',
             'mavericksnails',
             'ninjahummus',
             'masticatelavender',
             'logorrheaomelette',
             'morassartichokes',
             'canoodlepretzel',
             'lozengeavocados',
             'flannelmussels',
             'flumesoda']

contents = ''

for name in usernames:
    contents += f"{name}\n"

path = Path('output.txt')
path.write_text(contents)