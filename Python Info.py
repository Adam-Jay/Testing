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

del var2  				#Deletes the variable (it will cease to exist and you cannot reference it anymore)
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

#--------------#
#--Comparison--#
#--------------#
5 == 5 	#Equals
4 != 5 	#Does not equal
3 > 2	#Greater than
3 >= 3 	#Greater than or equal to
2 < 3 	#Less than
3 <= 3 	#Less than or equal

#Not just numbers can be compared... strings can be compared lexicographically
"a" < "b"
"Zebra" < "Zylophone"
"Tim" < "Timothy"

#--------------#
#--Conditions--#
#--------------#
condition = False

'''Evaluates the condition(s) of the statement, and IF it's true, then it executes the conditional code.
If it's not true, then it ignores the indented code.'''
if condition == True:
	print("The condition is true!")

#Else statements execute if the first statement was not true
if 1 > 2:
	print("1 is greater than two! \n")
else:
	print("1 is not greater than two! \n")

'''Nested statements. The output of this code is actually 3, not seven, since once the "var < 5"
condition is not met, it stops everything past it, EVEN IF it would be true.'''
var = 7
if var > 3:
   print("var > 3")
   if var < 5:
      print("var < 5")
      if var == 7:
         print("var == 7")

'''Elif (short for else if) statements are evaluated if the original if statement wasn't true.
The else is executed if none of the above statements are true.'''
if var == 3:
	print("var is 3 \n")
elif var == 7:
	print("var is 7 \n")
else:
	print("var isn't 3 or 7 \n")

#Remember that if the original if is true, the elif isn't executed even if it's true also!
if 1 == 1:
	print("One equals one. \n")
elif 2 == 2:
	print("Two equals two. \n")

#---------------------#
#--Boolean Operators--#
#---------------------#
#Only outputs true if BOTH inputs are true
if 1 == 1 and 2 == 2:
	print(True)

#Outputs if at least one is true
if 1 == 1 or 2 == 3:
	print(True)

#Outputs if the input is false
if not 1 == 5:
	print(True)

'''Note: The moment that the computer comes across something that can confirm an output, the rest after it
can and will be ignored. For example, if the first input into the OR is true, the whole thing is
automatically true without the rest even needing to be evaluated. The opposite is true for AND. If the
first condition is false, the whole thing is false without taking anything else into consideration.
This type of decision-making is called short-circuit evaluation.'''

#Operator precedence: which operators python evaluates first
False == False or True
	#True
False == (False or True)
	#False
(False == False) or True
	#True

#Math is done before the comparison.
2 + 3 == 5

'''Since this can often become very complicated, use parentheses even if they're not strictly neccesary!
1. First step is PEMDAS. Exponents, division, etc. are solved first.
2. Comparisons (ex. <=), then equalites (==), are then evaluated.
3. Afterwards, the logical operators are used. They DO NOT go from left to right like you might think.
   NOT is done first, then AND, then OR.'''

print("The output is " + str(True and not False))		#Outputs True
							#True and(not False)

print("The output is " + str(False or True and False))	#Outputs False
							#False or(True and False)
print("")

#---------#
#--Loops--#
#---------#
#The while loop is like an if, but can occur (iterate) many times. It continues as long as it's true.
i = 1			#The variable "i" is set as the loop counter variable and is incremented at each iteration.
while i < 5:	#It prints the number on each repetition, NOT including 5. Once it's no longer less than 5,
	print(i)	#it stops.
	i += 1

#Infinite loops always remain true (but can lead to freezing since they never end)
#while True:
#	print("INFINITE")

#The break statement terminates a loop immediately.
while True:
	break
	print("This is some text!")

#How many times does this loop print? (Answer: 3)
i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

#The continue statement restarts the loop
while i > 0:
	i -= 1
	print("Hello")
	continue
	print("Hi")

#-------------------#
#--Lists--(Arrays)--#
#-------------------#
#Create an indexed list of items which can be accessed using the name of the list and the index in brackets
to_do = ["Study", "Read", "Brush teeth"]
print(to_do[1])

#You can even print the entire array at once!
print(to_do)

#You can initialize a list with nothing in it with empty square brackets:
empty_list = []

#You can fill lists with lots of data types, including nested lists!
new_list = ["string", 5.3, 2, False, [0, 1, 2, 3]]
print(new_list[4][3])

#Strings can even be indexed like lists!
string_variable[2]

#Reassigning a value in a list
new_list[2] = 50

#Accessing multiple vales of lists or strings
new_list[1:3]
"Hello World"[4]

#You can even concatenate and multiply lists like strings!
new_list = new_list + ["Other", "Stuff"]
new_list = new_list * 2

#"in" checks if something is in a list or string.
5.15 in new_list
"Hello" in "Hello, World!"

another_list = ["Hello", "darkness my old friend", ["item1", "item2"]]
"darkness" in another_list		#False: it expects to find an index with EXACTLY this as its value
"darkness" in another_list[1]	#True: tells it to specifically look into this index for the substring
"item1" in another_list			#False: does not search inside nested lists
"item1" in another_list[2]		#True

#To check if it's not in a list, you can do it two ways
"foo" not in new_list
not("foo" in new_list)

#Editing a list
numbers = [1, 2, 3]
numbers.append(4)		#Only one at a time
numbers += [5, 6]		#Multiple at a time
numbers.insert(3, 3.5)	#Inserts value at the given index

numbers.remove(3.5)		#Removes the index containing the first occurence of this value in the list
numbers.pop()			#Remove and return the value of the given index (last index by default)
del numbers[4]			#Removes the given index

#More things to do with lists
len(new_list)					#Finds the legnth of the list
new_list.index("Stuff")			#Returns the index of the first occurence of the value "Stuff"
"Hello World".index("o", 5)		#Can also set where to look / start looking
new_list.count("String")		#Finds how many indexes are that value

#Note that you can't compare numbers to strings or it will produce an error
max(numbers)		#Gives the max (highest number or last in the alphabet)
min(numbers)		#Gives the min (lowest number or first in the alphabet)
numbers.sort()		#Sorts the list
numbers.reverse()	#Reverses the list

new_list.clear()	#Empties out the list

#---------#
#--Range--#
#---------#
#Creates a list with values starting with 10 and ending with (BUT not including) 13 with an increment of 1
range_list = list(range(10, 13, 1))
print(range_list)

range(5)	#Creates a range of all integers starting at zero and ending at (NOT including) 5

#---------#
#--Input--#
#---------#
user_input = input("\nWhat's your name? ")	#Asks for information from the user with the given prompt
print("Hello,", user_input, "!")			#Outputs the information the user gave
