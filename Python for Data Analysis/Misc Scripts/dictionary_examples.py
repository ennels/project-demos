#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment 5 - Dictionaries
print("\n\n------------------------------------------")

# Section 1

print("--------------- SECTION 1 ----------------\n------------------------------------------\n")

dictionary = {'name': 'elijah walker','age': 'twenty-three','city': 'mccall'}
print(f"Here is a dictionary of strings:\n\n\t{dictionary}\n")

dictionary['state'] = 'idaho'
print(f"A new key-value pair has been added:\n\n\t{dictionary}\n")

dictionary['age'] = 23
print(f"One of the values has been updated into an integer:\n\n\t{dictionary}\n")

del dictionary['city']
print(f"One of the key-value pairs has been deleted:\n\n\t{dictionary}\n")

print(f"Accessing one value in the dictionary:\n\n\t{dictionary['name'].title()}\n")

print(f"Accessing a value with the .get() method:\n\n\t{dictionary.get('age')}\n")

print(f"Using the .get() method to account for key index failure:\n\n\t{dictionary.get('height', 'Key not found')}\n")

# Section 2

print("\n------------------------------------------\n--------------- SECTION 2 ----------------\n------------------------------------------\n")

print("Looping through all keys in the dictionary:\n")
for key in dictionary.keys():
    print(f"\t{key}")
    
print("\nLooping through all values in the dictionary:\n")
for value in dictionary.values():
    print(f"\t{value}")

print("\nLooping through all key-value pairs in the dictionary:\n")
for key, value in dictionary.items():
    print(f"\t{key}\t| {value}")

print("\nLooking through all key-value pairs in a sorted order:\n")
for key in sorted(dictionary.keys()):
    print(f"\t{key}\t| {dictionary[key]}")

# Section 3

print("\n\n------------------------------------------\n--------------- SECTION 3 ----------------\n------------------------------------------\n")

print("Creating a dictionary of dictionaries:\n")
employees = {
    'e_walker': {
        'name': 'elijah walker',
        'age': 23,
        'city': 'mccall'
    },
    'm_matthews': {
        'name': 'madeline matthews',
        'age': 22,
        'city': 'oakland'
    },
    'j_mason': {
        'name': 'jeremiah mason',
        'age': 20,
        'city': 'newberg'
    }
}
for employee in employees:
    print(f"\t{employee}")
    print(f"\t\t{employees[employee]}\n")

print("\nAccessing items in those dictionaries:\n")
for employee in employees:
    print(f"\t{employees[employee]['name'].title()} is {employees[employee]['age']} years old and lives in {employees[employee]['city'].title()}.")


print("\nCreating a list of dictionaries:\n")
employees = [
    {'name': 'elijah walker', 'age': 23, 'city': 'mccall'},
    {'name': 'madeline matthews', 'age': 22, 'city': 'oakland'},
    {'name': 'jeremiah mason', 'age': 20, 'city': 'newberg'}
]
for employee in employees:
    print(f"\t{employee}")

print("\nAccessing items in those dictionaries:\n")
for employee in employees:
    print(f"\t{employee['name'].title()} is {employee['age']} years old and lives in {employee['city'].title()}.")

print("\n\n------------------------------------------")