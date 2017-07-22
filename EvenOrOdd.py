#EvenOrOdd.py
#Adam Jay
#The program determines if the user-entered number is even or odd.
#TO-Do: Make sure the user's input is a number

#Asks for input and assigns it to the variable "number" as an integer.
number = int(input("Enter a number: "))

#If there is no remainder between the number and two, then it must be even.
if (number % 2) == 0:
    print("The number is even. ")

#Otherwise, the number is odd.
else:
    print("The number is odd. ")
