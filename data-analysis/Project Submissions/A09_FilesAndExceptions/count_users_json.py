#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Files and Exceptions
from pathlib import Path
import json

# ALL FILES FOR SECTION 4 ARE WRITTEN WITH THE SAME CODE.
# I WAS TOO LAZY TO SPLIT THIS FILE UP INTO SMALLER ONES.
# I was also too lazy to create a dedicated JSON storage function,
# which, in retrospect, probably coulda saved me time...

# Storing, reading, printing, counting, and searching for usernames within a JSON file

path = Path("users.json")
storage = ['']
with open(path, 'r', encoding="utf-8") as f:
    if len(path.read_text(encoding="utf-8")) == 0:
        print(f"\nFile '{path}' is empty/missing. Fixing...\n")
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(storage, f)


def take_command(user_input):
    '''Takes user input and performs the corresponding action.'''

    if user_input == 'quit':
        quit()

    try:
        # Found this trick online
        with open(path, 'r', encoding="utf-8") as f:
            storage = json.load(f)

    except json.JSONDecodeError:
        pass

    print()

    if user_input == 'count':
        count = len(storage)
        if storage == ['']:
            count = 0
        print(f"\nTotal usernames stored in '{path}': {count}\n")

    elif user_input == 'show':
        try:
            print("\nStored Usernames:\n")

            if storage == ['']:
                raise UnboundLocalError

            elif '' in storage:
                storage.remove('')

            for item in storage:
                print(f"\t{item}")

        except UnboundLocalError:
            print("\tThe file is empty. Add some users!")

    elif user_input == 'add' or user_input == 'search' or user_input == 'delete':
        search = input("\nEnter a username: ").lower()

        if search in storage:
            if user_input == 'delete':
                if user_input != '':
                    storage.remove(search)
                    with open(path, 'w', encoding="utf-8") as f:
                        json.dump(storage, f)
                        print(f"\nUsername '{search}' deleted from '{path}'.\n")
                else:
                    print("\nNo username entered. Please try again.\n")

            elif user_input == 'search' and user_input != '':
                print(f"\n'{path}' contains user '{search}'.\n")

            elif user_input == 'add':
                print(f"\nUsername '{search}' already exists in the file.\n")

        else:
            if user_input == 'search' or user_input == 'delete':
                print(f"\n'{path}' does not contain user '{search}'.\n")

            else:
                storage.append(search)
                if [''] in storage:
                    storage.remove('')

                try:
                    with open(path, 'w', encoding="utf-8") as f:
                        json.dump(storage, f)
                        print(f"\nUsername '{search}' added to '{path}'.\n")

                except Exception as message:
                    print(message)

    else:
        print("Invalid command. Please try again.")


while True:

    print("\n------------------------------------------")

    take_command(input("\n\n- ENTER A COMMAND -\n\n"
                       "Add:\t\tAdd a new user\n"
                       "Delete:\t\tDelete a saved user\n"
                       "Count:\t\tTotal number of users in file\n"
                       "Search:\t\tSearch for a saved user\n"
                       "Show:\t\tDisplay JSON file contents\n"
                       "Quit:\t\tQuit program\n\n\t").lower())
