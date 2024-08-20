# Arithmetic Operations #
#**Learning objectives**
#
#After this section:
#
# * You will be able to use variables in various arithmetic operations
# * You will know how to deal with numbers in user input
# * You will know how to cast values into other fundamental data types

#   |Operator	|Purpose							|Example	|Result	|
#   |+			|Addition							|2 + 4		|6		|
#   |-			|Subtraction						|10 - 2.5	|7.5	|
#   |*			|Multiplication						|-2 * 123	|-246	|
#   |/			|Division (floating point result)	|9 / 2		|4.5	|
#   |//			|Division (integer result)			|9 // 2		|4		|
#   |%			|Modulo								|9 % 2		|1		|
#   |**			|Exponentiation						|2 ** 3		|8		|

## Live Demo ##
# Multiple Operations
#height = 172.5
#weight = 68.55
## the Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
## height is converted into metres in the formula
#bmi = weight / (height / 100) ** 2
#print(f"The BMI is {bmi}")
#
# Int vs Float Division
#x = 3
#y = 2
#
#print(f"/ operator {x/y}")
#print(f"// operator {x//y}")
#
# Casting
#input_str = input("Which year were you born? ")
#year = int(input_str)
#print(f"Your age at the end of the year 2021: {2021 - year}" )
#
#year = int(input("Which year were you born? "))
#print(f"Your age at the end of the year 2021: {2021 - year}" )
#
#height = float(input("What is your height? "))
#weight = float(input("What is your weight? "))
#height = height / 100
#bmi = weight / height ** 2
#print(f"The BMI is {bmi}")


## Problem 1 ##
#Please write a script that: 
# - Asks for 2 numbers
# - Prints out those numbers dividing with int division and float division



## Problem 2 ##
#Please write a script that: 
# - Asks user for their name and year of birth
# - Prints something like:
# Sample output:
# --------------------------------------------------
#  What is your name? Frances Fictitious
#  Which year were you born? 1990
#  Hi Frances Fictitious, you will be 31 years old at the end of the year 2021


## Problem 3 ##
#Please rewrite this script so that it only uses 2 variables. It should retain its original behavior 
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

sum = number1 + number2 + number3
print(f"The sum of the numbers: {sum}")


## Problem 4 ##
#Please write a program that:
# - Asks the user for a number of days. 
# - Prints out the number of seconds in the amount of days given.



## Problem 5 ##
#Please write a program that:
# - Asks the user for 4 numbers
# - Prints out the sum and mean (average) of the numbers





## Problem 6 ##
#Please write a program that:
# - Asks the user for 
#   - Number of Students
#   - Group size
# - Prints out the number of groups formed using those inputs
#   - If the division is not even, one of the groups may have fewer members than specified.
# - Hint: the integer division operator // could come in handy here.
# ---------------------------------------
#Sample output
#How many students on the course? 8
#Desired group size? 4
#Number of groups formed: 2
#
#Sample output
#How many students on the course? 11
#Desired group size? 3
#Number of groups formed: 4
#
#