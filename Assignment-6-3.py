# More about variables #
#**Learning objectives**
#
#After this section:
#
#* You will be able to use variables in different contexts
#* You will know what kind of data can be stored in variables
#* You will understand the difference between strings, integers and floating point numbers



## Live Demo ##
#
# Casing
#name = input("What is your name? ")
#Name = input("What is your name? ")
#print(name)
#print(Name)
#
# Talk about Variable Types
#   * int vs string vs float
#intNum = 75
#print(intNum/2)
#number = "100"
#print(number / 2)
#number1 = 2.5
#number2 = -1.25
#number3 = 3.62
#
#print(f"Mean: {mean}")
#mean = (number1 + number2 + number3) / 3
#
# Printing different types and Casting
#result = 10 * 25
#print("The result is " + result)
#print("The result is " + str(result))
#print("The result is", result)
#print(f"The result is {result}") # Format string {} denotes values to be printed
#name = "Mark"
#age = 37
#city = "Palo Alto"
#print(f"Hi {name}, you are {age} years old. You live in {city}.")
#
# Printing invisible things
#print("\n") # newline
#print("\t") # tab
#print("\\") # \


## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 euros per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is ", name, " , I am ", age, "years old")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")")
print("- ", skill3, " (", level3, " )")
print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")





## Problem 2 ##
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = input("X val: ")
y = input("Y val: ")

