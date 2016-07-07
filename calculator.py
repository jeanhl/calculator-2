"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    """ This is a calculator interface

    This function asks the user to type in a math expression using prefix notation and 
    based on the type of operator calls the approrpriate function to perform the calculation
    """ 

    #asks for user's input 
    user_input = raw_input("Type in the math expression and two numbers like + 1 2 : ")
    #splits the user's input into a list
    math_op = user_input.split(" ")

    #pulls the appropriate function based on the user's input
    if math_op[0] == '+':
        print add(int(math_op[1]), int(math_op[2]))

    elif math_op[0] == '-':
        print subtract(int(math_op[1]), int(math_op[2]))

    elif math_op[0] == '*':
        print multiply(int(math_op[1]), int(math_op[2]))

    elif math_op[0] == '/':
        print divide(int(math_op[1]), int(math_op[2]))
    
    elif math_op[0] == "square":
        print square(int(math_op[1]))

    elif math_op[0] == 'cube':
        print cube(int(math_op[1]))

    elif math_op[0] == 'pow':
        print power(int(math_op[1]), int(math_op[2]))

    elif math_op[0] == 'mod':
        print mod(int(math_op[1]), int(math_op[2]))

    else:
        print "That is not a valid input. Please try any of the following operator: + - * / square cube pow mod."


#calls function calculator
calculator()