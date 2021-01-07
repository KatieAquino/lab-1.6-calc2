"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
#   #ask user fo input 
#    read input
#     tokenize input
#         if the first token is "q":
#             quit
#         elif: (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             repeat for operatiors: "+", "-", "*", "/", "square", "cube", "mod"
#         else:
#             print statement saying invalid operator, and repeat loop


# tokens = input_string.split(' ')   # => ['pow', '3', '5']
# input_string = 'pow 3 5'
# print(find_operator())

# Ask user function
# find operator
# run calc 


def find_operator():
    while True:
        input_string = input("Please enter your operator followed by two numbers. If using square or cube, only enter one number: ")
        # this variable creates list of three string items
        tokens_list = input_string.split(' ')
        op_var = tokens_list[0]
            

        if op_var.lower() == 'q': #if user enters a 'q' or 'Q' in first spot, will quit calculator
            return "Sorry to see you go!" 

        elif op_var == "+" or op_var.lower() == "add": #if user enters a + or "add" in any case will call the add function
            num1 = int(tokens_list[1])
            num2 = int(tokens_list[2])
            print(add(num1, num2))

        elif op_var == "-" or op_var.lower() == "sub": # if user enters a - or 'sub' in any casee will call subtract function
            num1 = int(tokens_list[1])
            num2 = int(tokens_list[2])
            print(subtract(num1, num2))

        elif op_var == "*" or op_var.lower() == "multiply": #if user enters a * or "multiply" in any case will call multiply function
            num1 = int(tokens_list[1])
            num2 = int(tokens_list[2])
            print(multiply(num1, num2))

        elif op_var == "/" or op_var.lower() == "div": #if user enters a / or "div" in any case will call divide function
                num1 = int(tokens_list[1])
                num2 = int(tokens_list[2])
                print(divide(num1, num2))

        elif op_var.lower() == "square" or op_var.lower() == "sq": #if user enters a "square" or "sq" will call square function
            num1 = int(tokens_list[1])
            print(square(num1))

        elif op_var.lower() == "cube": #if user enters a "cube" will call cube function
            num1 = int(tokens_list[1])
            print(cube(num1))

        elif op_var == "**" or op_var.lower() == "pow": #if user ** or power will call power function
            num1 = int(tokens_list[1])
            num2 = int(tokens_list[2])
            print(power(num1, num2))

        elif op_var == "%" or op_var.lower() == "mod": #if user enters % or mod will call mod function
            num1 = int(tokens_list[1])
            num2 = int(tokens_list[2])
            print(mod(num1, num2))

        else:
            print("Sorry. Check your syntax and try again :(") #if they enter something we did not account for will start the user over again.

find_operator()