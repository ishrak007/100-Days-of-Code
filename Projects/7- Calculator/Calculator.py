operation_list = ["+", "-", "*", "/", "^", "%", "gcd", "//"]

import math
from calc_arts import *
from replit import clear
print(logo)

def error_checker_op(op_str):
    if op_str not in operation_list:
        print("Invalid Key. Try Again.")
        return error_checker_op(input("Pick an operation: "))
    else:
        return op_str

def calc(n1, operator, n2):
    if operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2
    elif operator == "*":
        return n1*n2
    elif operator == "/":
        return n1/n2
    elif operator == "^":
        return n1**n2
    elif operator == "%":
        return n1%n2
    elif operator == "gcd":
        return math.gcd(int(n1), int(n2))
    elif operator == "//":
        return n1//n2
    
def continuous_op(str, prev_result):
    if str == 'n':
        clear()
        a = float(input("What's the first number? "))
        print(operations_art)
        operation = error_checker_op(input("Pick an operation: "))
        b = float(input("What's the next number? "))
        result = calc(n1=a, n2=b, operator=operation)
        print(f"{a} {operation} {b} = {result}")
        print(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'e' to exit")
        cont_statement = input("How do you want to proceed? ")
        continuous_op(cont_statement, result) 
    elif str == 'y':
        m = prev_result
        print(f"Previous result = {m}")
        print(operations_art)
        operation = error_checker_op(input("Pick an operation: "))
        n = float(input("What's the next number? "))
        result = calc(n1=m, n2=n, operator=operation)
        print(f"{m} {operation} {n} = {result}")
        print(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'e' to exit")
        cont_statement = input("How do you want to proceed? ")
        continuous_op(cont_statement, result)
    elif str == 'e':
        print("Goodbye")
    else:
        print("Invalid Key. Try Again.")
        cont_statement = input("How do you want to proceed? ")
        continuous_op(cont_statement, result)
        
# Initial display
a = float(input("What's the first number? "))
print(operations_art)
operation = error_checker_op(input("Pick an operation: "))
b = float(input("What's the next number? "))
result = calc(n1=a, n2=b, operator=operation)
print(f"{a} {operation} {b} = {result}")
print(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'e' to exit")
cont_statement = input("How do you want to proceed? ")
continuous_op(cont_statement, result)
