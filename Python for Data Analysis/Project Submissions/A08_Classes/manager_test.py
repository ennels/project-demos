#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment 8 - Classes

import random
from employee import Manager, 

managers = [
    ("Sue Davis", "Manager", 27, 5.5),
    ("Reginald King", "Manager", 25, 7),
    ("Herald Walker", "Manager", 23, 10)
]

print("\n--------------------------------------")
print("----------- Payroll time! ------------")
print("--------------------------------------\n")

for each in managers:
    name, position, salary, bonus = each
    manager = Manager(name, position, salary, bonus)
    manager.about()
    manager.pay(random.randint(30, 50))
    print("\n--------------------------------------\n")
