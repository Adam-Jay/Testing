#Division.py
#Adam Jay
#The goal of this is to find other ways of performing division, floor, and mod.

#---------#
#--Setup--#
#---------#
#Assigns values to the number to be divided (num1) and the number to divide by (num2)
num1 = -250
num2 = 5
print("Number to be divided: ", num1)
print("Number to divide by:", num2, "\n")

#------------#
#--Division--#
#------------#
#Divides using python
quotient = num1 / num2

#Outputs the result
print("Answer:", quotient)

#---------#
#--Floor--#
#---------#
#Floor using python
floor_division = num1 // num2

#Converting to an integer simply truncates the decimal like floor division does
floor_division = int(num1 / num2)

#Manually truncate the float by finding the position of the decimal outputting all BEFORE it
quotient_string = str(num1 / num2)
decimal_spot = quotient_string.find(".")
floor_division = quotient_string[0:decimal_spot]

#Output the result
print("Result of floor division:", floor_division)

#-------#
#--Mod--#
#-------#
#Mod using python
mod = num1 % num2

#If the rounded result is equal to the non-rounded, it has no remainder
if round(quotient) == quotient:
	mod = 0

#If the spot after the decimal is a zero (since it's a float), it has no remainder
if quotient_string[decimal_spot + 1] == str(0):
	mod = 0

'''The mod is the (abs of the) difference between the floor division times the number divided by
and the number that was divided.'''
mod = abs(num1 - (int(floor_division) * num2))

#Output the result
print("Remainder of calculation:", mod)

#-----------------#
#--Long division--#
#-----------------#
'''
RULES OF long division:
	!!!!!!!!!!!!!!!!!!!!!! WIP

To find the floor with long division, just do it
To find the mod (remainder) with long division, subtract the final answer from the number divided by and the number that was divided
Do find the exact answer, take the floored answer, and add the remainder over what was divided by
'''