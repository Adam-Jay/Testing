#Python Info.py
#Adam Jay
#Just basic python code... It's here for my reference! :)

#---------#
#--Setup--#
#---------#
#Imports some useful methods and info that can be used later
import random, math, sys, os

#-------------#
#--Variables--#
#-------------#
#Variables are case-sensitive and cannot begin with numbers
var = 10			#Initializing: The variable var is declared and the value of 10 is assigned to it
var = 50 			#The variable var's value is reassigned
var2 = var = 600	#You can assign the same value to multiple variables simultaneously

integer_variable = 3 	#Non-decimal number
float_variable = 3.14 	#Decimal number
boolean_variable = True	#True or False
string_variable = "Hi!"	#Sequence of characters

del var  				#Deletes the variable (it will cease to exist and you cannot reference it anymore)
print(integer_variable)	#When you reference a variable, it returns the value stored in it.

#-----------#
#--Strings--#
#-----------#
print("You can create a new line \nlike this! \n")

print("You can prevent a new line from being created at the end ", end = "")
print("like this! \n")

print("\"Slashes allow you to put in quotes\" - Abraham Lincoln \n")

print("""Multi-lined quotes are created with three quotation marks.
They can be pretty useful sometimes!
'''Multi-lined comments use
apostrophes'''
""")

print("You can multiply strings by integers! \n" * 3)

#-----------#
#--Casting--#
#-----------#
#Casting is when you convert one datatype to another
print("int(4.6) = ", int(4.6)) 		#Truncates (cuts off the decimal)
print("float(30) = ", float(30))	#Adds a decimal to make it a float
print("str(52.62) = ", str(52.62))	#Converts it into a string

print("")

print("int(5) + int(6) = ", int(5) + int(6))			#Adds the two integers
print("float(5) + float(6) = ", float(5) + float(6))	#Adds the two floats to produce a float answer
print("str(5) + str(6) = ", str(5) + str(6))			#Concatenates (joins) 5 and 6 to produce 56

print("")

#--------------#
#--Operations--#
#--------------#
print("5 + 2 =", 5 + 2)		#Addition
print("5 - 2 =", 5 - 2)		#Subtraction
print("5 * 2 =", 5 * 2)		#Multiplication
print("5 / 2 =", 5 / 2)		#Division
print("5 // 2 =", 5 // 2)	#Floor division (divides, then rounds down)
print("5 % 2 =", 5 % 2)		#Mod (finds remainder)
print("5 ** 2 =", 5 ** 2)	#Exponent

print("")

print("10 / 2 = 5.0")		#All division yields floats
print("2 + 3.0 = 5.0")		#Using floats turns the answer into a float

print("")

var = var + 5	#Long way
var += 5 		#Shortcut

#Don't forget about PEMDAS! (operator precedence hierarchy)
5 + 80 * 2
(5 + 80) * 2

#--------#
#--Math--#
#--------#
math.pi				#Outputs PI

round(1.14)			#Rounds to the nearest 10th
round(3.432, 0)		#Rounds to the specified place
math.ceil(4.2)		#Rounds up
math.floor(4.8)		#Rounds down

math.sqrt(64)		#Square root
abs(-5)				#Absolute value

math.sin(40)		#Sine 	 (in rad)
math.cos(40)		#Cosine  (in rad)
math.tan(40)		#Tangent (in rad)

math.asin(0.5)		#Arcsine   (sin inverse)
math.acos(0.5)		#Arccosine (cos inverse)
math.atan(0.5)		#Arctangent(tan inverse)

math.degrees(1.5)	#Converts rad to degrees
math.radians(60)	#Converts degrees to rad

math.log(50, 5)		#Log base 5 of 50
math.log10(100)		#Log base 10
math.log(42)		#Natural log
math.exp(5)			#Outputs e to the power of the given value

max(2, 40)	#Outputs the largest number  (can input array also)
min(4, -1)	#Outputs the smallest number (can input array also)

random.seed()				#Sets the random seed
random.random()				#Outputs a float between 0 and 1 (MANY decimal places)
random.randrange(3, 100)	#Gets a random integer >= 3 and < 100
random.randint(3, 100)		#Same as above but inclusive (can = 100)

#---------#
#--Input--#
#---------#
user_input = input("What's your name? ")	#Asks for information from the user with the given prompt
print("Hello,", user_input, "!")			#Outputs the information the user gave