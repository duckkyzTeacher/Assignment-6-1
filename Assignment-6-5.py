# Conditional Statements #
#**Learning objectives**
#
#After this section:
#
# * You will be able to use a simple conditional statement in programming
# * You will know what a Boolean value is
# * You will be able to express conditionals with comparison operators

|Operator	| Purpose					| Example	|
|==			| Equal to					| a == b	|
|!=			| Not equal to				| a != b	|
|>			| Greater than				| a > b		|
|>=			| Greater than or equal to	| a >= b	|
|<			| Less than					| a < b		|
|<=			| Less than or equal to		| a <= b	|


## Live Demo ##
# if statements
#age = int(input("How old are you? "))
#if age > 17:
#    print("You are of age!")
#    print("Here's a copy of GTA6 for you.")
#print("Next customer, please!")
#
#number = int(input("Please type in a number: "))
#
#if number < 0:
#    print("The number is negative.")
#
#if number > 0:
#    print("The number is positive.")
#
#if number == 0:
#    print("The number is zero.")
#
# Boolean type
#a = 3
#condition = a < 5
#print(condition)
#if condition:
#    print("a is less than 5")
#
#condition = True
#if condition:
#    print("This is printed every time.")
#


## Problem 1 ##
#Please write a script that: 
# - Asks the user for an integer number. 
# - If the number is less than zero, the program should print out the number multiplied by -1. 
# - Otherwise the program prints out the number as is.



## Problem 2 ##
#Please write a script that: 
# - Asks user for their name
# - if the users name is anything but "Plankton", the program then asks for the number of Krabby Patties and prints out the total cost.
# 	- The price of a single portion is 5.90.
# Sample output:
# --------------------------------------------------
#    Please tell me your name: Gary
#    How many Krabby Patties? 2
#    The total cost is 11.8
#    Next please!
#    
#    Please tell me your name: Plankton
#    Next please!


## Problem 3 ##
#Please write a script that: 
# - Asks the user for two numbers and an operation.
# - If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. 
# - If the user types in anything else, the program should print out nothing
# Sample output:
# --------------------------------------------------
#    Number 1: 10
#    Number 2: 17
#    Operation: add
#    
#    10 + 17 = 27
#    
#    Sample output
#    Number 1: 4
#    Number 2: 6
#    Operation: multiply
#    
#    4 * 6 = 24


## Problem 4 ##
#Please write a program that:
# - Asks for the hourly wage, hours worked, and the day of the week. 
# - The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.



## Problem 5 ##
#Please write a program that:
# - Solves a quadratic equal of the form ax²+bx+c
# - The program asks for values a, b and c. 
# - It should then use the quadratic formula to solve the equation
#   - x = (-b ± sqrt(b²-4ac))/(2a).
# Sample output:
# --------------------------------------------------
#   Value of a: 1
#   Value of b: 2
#   Value of c: -8
#   
#   The roots are 2.0 and -4.0
from math import sqrt   # this imports the sqrt function
print(sqrt(9))
