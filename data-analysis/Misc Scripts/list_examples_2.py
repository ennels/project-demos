#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment 3 - Working with Lists
print("\n\n------------------------------------------")

# Section 1 - Looping Through a List

print("--- SECTION 1 - LOOPING THROUGH A LIST ---\n------------------------------------------\n")
family = ["jon", "sara", "elijah", "jacob", "benjamin", "lucy", "leia"]
print(f"Here is a list with my family members:\n    {family}\n")

print("Here they are, listed with a 'for' loop:\n")
counter = 1    # Just a counter to number the family members
for member in family:
    print(f"    Member {counter}: {member.title()}")
    counter += 1

print(f"\n    Total family members: {len(family)}\n\n\n")


# Section 2 - Range Functions

print("-----------------------------------------\n------ SECTION 2 - RANGE FUNCTIONS ------\n-----------------------------------------\n")
print(f"Here is an integer list created with list and range functions:\n\n    {list(range(1, 9))}\n")

print("And here are the values listed with a range function in a 'for' loop:\n")
for value in range(1, 6):
    print(f"    {value}")

every_third = list(range(1, 26, 3))
print(f"\nHere is a list of every third value from 1 to 25:\n\n    {every_third}\n")

cubes = [value**3 for value in range(1, 11)]
print(f"Here is a list of the cubed values of numbers from 1 to 10:\n\n    {cubes}\n")

halves = [value / 2 for value in range(1, 11)]
print(f"Here is a list of the halved values of numbers from 1 to 10:\n\n    {halves}\n\n\n")


# Section 3 - Slicing a List

print("------------------------------------------\n------- SECTION 3 - SLICING A LIST -------\n------------------------------------------\n")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(f"Here is a list of colors:\n\n    {colors}\n")
print(f"Here are the first 3 list values:\n\n    {colors[0:3]}\n")
print(f"Here are the last 3 list values:\n\n    {colors[3:]}\n")
print(f"Here are the last 3 list values again, called with a negative index:\n\n    {colors[-3:]}\n")
print("Here are the middle 4 list values printed with a 'for' loop:\n")
for value in colors[1:5]:
    print(f"    {value.title()}")
print("\n\n")

# Section 4 - Copying a List

print("------------------------------------------\n------- SECTION 4 - COPYING A LIST -------\n------------------------------------------\n")
print("Slicing can also be used to create new, copied lists from existing ones!\n")
my_list = ['apples', 'bananas', 'cherries']
print(f"For example: Here is a list called 'my_list':\n\n    {my_list}\n")
print("Now you might be tempted to 'copy' the list like this:\n\n    your_list = my_list\n")
print("But that doesn't actually create a new list, it just creates a new REFERENCE to the OLD list!\n")
print("So if you change a value in 'your_list', it will also change the original, corresponding value in 'my_list'.\n")
print("I'll show you what I mean. Here are our two lists side-by-side:\n")
your_list = my_list
print(f"    my_list: {my_list}\n    your_list: {your_list}\n")
print("Now let's change the first item in 'your_list' to 'oranges'. Notice it happens to my_list as well!\n")
your_list[0] = 'oranges'
print(f"    my_list: {my_list}\n    your_list: {your_list}\n")
print("To actually create a new list, you need to use slicing to copy the entire list like this:\n\n    your_list = my_list[:]\n")
my_list = ['apples', 'bananas', 'cherries']
your_list = my_list[:]
print("So let's reset our lists, and change the first item in 'your_list' to 'oranges' again.\n")
print("Notice that my_list doesn't change this time!\n")
your_list[0] = 'oranges'
print(f"    my_list: {my_list}\n    your_list: {your_list}\n\n\n")


# Section 5 - Tuples (apparently you dont need parentheses?)

print("------------------------------------------\n----------- SECTION 5 - TUPLES -----------\n------------------------------------------\n")

tuple = 'True', 'False'
print(f"Tuple with two values:\n\n    {tuple}\n")

tuple_2 = 10, 
print(f"Tuple with one value:\n\n    {tuple_2}\n")

tuple_3 = 100, 200, 300, 400, 500
print(f"Tuple with multiple values:\n\n    {tuple_3}\n")

print("Multi-value tuple printed with a 'for' loop:\n")
counter = 1    # Just another counter to number the values
for value in tuple_3:
    print(f"    Value {counter}: {value}")
    counter += 1
    
print("\n\n------------------------------------------")