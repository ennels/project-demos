#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment 8 - Classes

# Section 1 - Basic Class
class Employee:
    '''A class to represent an employee.'''

    def __init__(self, name, position, salary, bonus):
        '''Initializes the employee with name, position, and salary.'''

        self.name = name
        self.position = position
        self.salary = salary
        self.bonus = bonus

    def about(self):
        '''Prints a string with employee details.'''

        print(f"\n{self.position.title()} Overview:\n"
              f"\n\tName:\t\t{self.name}\n\tPosition:\t{self.position}\n"
              f"\tSalary:\t\t${self.salary}")

    def pay(self, hours):
        '''Prints the weekly pay of the employee.'''

        print(f"\n\n{self.name.split()[0]}'s weekly pay:\n\n"
              f"\tHOURS\tRATE\tTOTAL\n")

        base_pay = round(self.salary * hours, 2)
        ot_pay = round(max(0, hours - 40) * self.salary * 1.5, 2)
        bonus_pay = round((base_pay + ot_pay) * (self.bonus / 100), 2)
        total_pay = round(base_pay + ot_pay + bonus_pay, 2)

        print(f"BASE:\t{hours}\t${self.salary}\t${base_pay}")

        if hours > 40:
            print(f"O/T:\t{hours - 40}\t${self.salary * 1.5}\t${ot_pay}")

        if self.bonus > 0:
            print(f"BONUS:\t--\t{self.bonus}%\t${bonus_pay}")

        if hours > 40 or self.bonus > 0:
            print(f"\t-----------------------\n"
                  f"\t\t\t${total_pay}\n\n")


# Section 2 - Inheritance
class Manager(Employee):
    '''A class to represent a manager. Inherits from Employee.'''

    def __init__(self, name, position, salary, bonus):
        '''Basically the same thing as with Employee.'''

        super().__init__(name, position, salary, bonus)
        self.bonus = bonus

    def about(self):
        '''Ditto, but includes bonus info.'''

        super().about()
        print(f"\tBonus:\t\t{self.bonus}%")

    def pay(self, hours):
        '''Prints the weekly pay of the manager, but includes bonus.'''

        super().pay(hours)
