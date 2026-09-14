#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment 8 - Classes

import random
from employee import Employee

employees = [
    ("Alice Johnson", "Developer", 25),
    ("Bob Smith", "Designer", 22),
    ("Charlie Brown", "General Employee", 15)
]

print("\n--------------------------------------")
print("----------- Payroll time! ------------")
print("--------------------------------------\n")

for each in employees:
    name, position, salary = each
    employee = Employee(name, position, salary)
    employee.about()
    employee.pay(random.randint(30, 50))
    print("\n--------------------------------------\n")
