# Section 1 - Access items in a list

futureCars = ["bmw m3 e30", "porsche boxter s", "ferrari enzo", "mitsubishi 3000gt vr4"]
print(f"Section 1:\n\n{futureCars[0]}")  # Accessing the first item
print(futureCars[len(futureCars)-1])  # Accessing the last item
print(f"{len(futureCars)}\n\n\n\nSection 2:\n\n")  # Getting the length of the list


# Section 2

futureCars = [item.title() for item in futureCars]  # Applying title case to each item in the list
print(futureCars)
futureCars.append("Toyota Supra")  # Appending an item to the end of the list
print(futureCars)
futureCars.insert(0, "Nissan Skyline R34")  # Inserting an item at the beginning
print(futureCars)
del futureCars[1]  # Removing the second item
print(f"{futureCars}\n\n\n\nSection 3:\n\n")


# Section 3

futureCars = ["bmw m3 e30", "porsche boxter s", "ferrari enzo", "mitsubishi 3000gt vr4"]
print("List reset.")
print(futureCars.pop(-1))  # Popping the last item
print(futureCars.pop(0))  # Popping the first item
futureCars.remove("porsche boxter s")  # Removing a specific item by value
print(f"{futureCars}\n\n\n\nSection 4:\n\n")


# Section 4

futureCars = ["bmw m3 e30", "porsche boxter s", "ferrari enzo", "mitsubishi 3000gt vr4"]

futureCars.sort() # Sort the list
print(futureCars)
futureCars = ["bmw m3 e30", "porsche boxter s", "ferrari enzo", "mitsubishi 3000gt vr4"]

futureCars.reverse()  # Reverse the list
print(futureCars)  # Print the reversed list
futureCars = ["bmw m3 e30", "porsche boxter s", "ferrari enzo", "mitsubishi 3000gt vr4"]

print(sorted(futureCars))  # Print a temporarily sorted list