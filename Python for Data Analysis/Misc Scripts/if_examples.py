#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment 4 - If Statements
print("\n\n------------------------------------------")

# Section 1 - Comparison Operators

print("---- SECTION 1 - COMPARISON OPERATORS ----\n------------------------------------------\n")

print("Comparison operators can be used to compare values and return boolean results (True or False).\n")

value_1 = 10
value_2 = 20

print(f"Here are two integer values:\n\n    value_1 = {value_1}\n    value_2 = {value_2}\n")
print("Here are some comparison examples between the two:\n")
print(f"    value_1 == value_2\n    {value_1 == value_2}\n")
print(f"    value_1 != value_2\n    {value_1 != value_2}\n")
print(f"    value_1 < value_2\n    {value_1 < value_2}\n")
print(f"    value_1 <= value_2\n    {value_1 <= value_2}\n")
print(f"    value_1 > value_2\n    {value_1 > value_2}\n")
print(f"    value_1 >= value_2\n    {value_1 >= value_2}\n\n\n")

blacklisted_users = ['elijah', 'jacob', 'ben', 'lucy']
print(f"You are in charge of a website. Here is a list of blacklisted users:\n\n    {blacklisted_users}\n")
print(f"User accessibility will be evaluated at login by the following:\n")
print ("    if login in blacklisted_users:\n        print('Sorry, you've been banned.')\n    else:\n        print('Welcome back!')\n\n")
print("Sara is logging in...\n")

login = 'sara'
if login in blacklisted_users:
    print(f"    Sorry, {login.title()}, you've been banned.\n\n")
else:
    print(f"    Welcome back, {login.title()}!\n\n")
print("Elijah is logging in...\n")

login = 'elijah'
if login in blacklisted_users:
    print(f"    Sorry, {login.title()}, you've been banned.\n\n")
else:
    print(f"    Welcome back, {login.title()}!\n")
print("Typical.\n\n")

# Section 2 - If Statements

print("------------------------------------------\n------- SECTION 2 -  IF STATEMENTS -------\n------------------------------------------\n")

print("If statements can be used to execute code based on conditions.\n")

print("Your age is 16. You're looking to get a driver's license in Idaho.\n")
age = 16
print(f"    age = {age}\n")
print("The minimum age limit for a driver's license in Idaho is 15.\n\nLet's check your eligibility with an 'if' statement:\n")

if age >= 15:
    print("    You are old enough to get your driver's license!\n\n")
print("Nice! You pass your test and buy a crappy sedan.\n")
print("Inspired by your newfound independence, you attempt to vote in the upcoming election.\n\nThe minimum age to vote in the U.S. is 18.\n\n\nLet's check your eligibility with an 'if-else' statement:\n")
if age >= 18:
    print("    You are old enough to vote!\n\n")
else:
    print(f"    Sorry, you've still got {18-age} years to wait.\n\n")
print("Bummer. You decide to pout at a ball game instead.\n\n")
print("Here are the entry rates to the game:\n")
print ("    CHILDREN 4 AND UNDER: FREE\n    KIDS: $5\n    ADULTS: $10\n\n")
print("Let's see if you qualify for discounted admission with an if-elif-else statement:\n")
if age < 4:
    print("    Your admission is free!\n\n")
elif age < 18:
    print("    Your admission is $5\n\n")
else:
    print("    Your admission is $10\n\n")
    
print("Not bad! Oh, to be young again.\n\n")

# Section 3 - Logic Operators

print("------------------------------------------\n------ SECTION 3 - LOGIC OPERATORS -------\n------------------------------------------\n")

print("Logical operators can be used to combine multiple conditions for evaluation within if statements.\n")
print("You're applying for a scholarship. This particular scholarship has some eligibility requirements:\n")
print("    1) You must be a U.S. citizen\n    2) You must have a GPA of 3.0 or higher\n    3) You must be enrolled full-time\n\n")

citizenship = True
gpa = 3.5
enrollment = 'full time'

print("Like a Pokémon, these are your stats:\n")
print("    citizenship = True\n    gpa = 3.5\n    enrollment = 'full time'\n\n")

print("Let's see if you qualify with an 'if' statement using the 'and' logical operator:\n")
if (citizenship == True) and (gpa >= 3.0) and (enrollment == 'full time'):
    print("    Congratulations! You qualify for the scholarship!\n\n")
else:
    print("    Sorry, you do not qualify for the scholarship.\n\n")

print("Whew! You made it. Now, let's see if you can get a work-study job on campus.\n")
print("The requirements for the job are:\n")
print("    1) You must live on-campus\n    \n    OR\n\n    2) You must have a commute time of 30 minutes or under\n\n")

housing = 'off campus'
commute_time = 15
print("In your situation:\n\n    housing = 'off campus'\n    commute_time = 15\n\n")

print("Let's see if you qualify with an 'if' statement using the 'or' logical operator:\n")
if (housing == "dorm") or (commute_time <= 30):
    print("    Congratulations! You qualify for the work-study job!\n\n")
else:
    print("    Sorry, you do not qualify for the work-study job.\n\n")
print("Sweet! You can now afford to eat something other than ramen.\n\n")

print("Fueled by frozen pizza and Mountain Dew, you decide to try your hand a summer internship.\n")
print("The only eligibility requirement is:\n\n    You must be passing all classes.\n")

grades = ['A-', 'B', 'A', 'C+', 'B-']
print("Here is a list of your letter grades for the semester:\n")
print(f"    {grades}\n\n")
print("Let's see if you qualify with an 'if' statement using the 'not' logical operator:\n")
if 'F' not in grades:
    print("    Congratulations! You qualify for the internship!\n\n")
else:
    print("    Sorry, you do not qualify for the internship.\n\n")
print("Yes! You can finally get some real-world experience and make some connections.\n\n")
print("Things are looking up for you as a student!\n\n")

print("------------------------------------------")