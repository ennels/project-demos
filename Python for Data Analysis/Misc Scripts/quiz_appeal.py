# Question 10
print("Question 10\n")
mylist = [10, 20, 30, 40, 50, 60]
print(f"mylist = {mylist}")
print(f"mylist[2:5] = {mylist[2:5]}")
print("My answer: [30, 40, 50]")
print("Quiz answer: [30, 40, 50, 60]\n\n")


# Question 11
print("Question 11\n")
mylist = [5, 6, 7, 8, 9]
print(f"mylist = {mylist}")
print(f"mylist[:3] = {mylist[:3]}")
print("My answer: [5, 6, 7]")
print("Quiz answer: [5, 6, 7, 8]\n\n")


# Question 13
print("Question 13\n")
print(f"mylist = {mylist}")
print("Now these changes are made:")
copy = list(mylist)
print("    copy = list(mylist)")
mylist[0] = 10
print("    mylist[0] = 10")
print(f"mylist = {mylist}")
print(f"copy = {copy}")
print("\nBecause 'copy' is a separate copy of the original list and does not "
      "change when the original list changes, it makes a copy 'correctly'.")
print("My answer: Both B (copy = mylist[:]) and C (copy = list(mylist))")
print("Quiz answer: copy = mylist[:]")

# I submitted this file as an appeal for questions I missed on a quiz.
# I received full credit for the questions after review.
