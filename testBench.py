#!/usr/bin/env python3
# import io
# import tokenize
# import ast
# 
# 
# code_snippet = """
# for i in range(10):
#     print(f"{i}")
#     if i == 2:
#         print(f"i is now 2")
#     else:
#         print(f"i is not 2")
# print("this is getting weird")
# """
# 
# syntax_tree = ast.parse(code_snippet)
# code_reader = io.StringIO(code_snippet)
# 
# for token_info in tokenize.generate_tokens(code_reader.readline):
#     token_type = token_info.type
#     token_lexeme = str(token_info.string)
#     start_line, start_col = token_info.start
#     end_line, end_col = token_info.end
#     original_line = token_info.line
# 
#     # You can get the human-readable name of the token type
#     # from the 'token' module (another built-in module)
#     import token
#     type_name = token.tok_name[token_type]
# 
#     #print(f"TYPE: {type_name:<15} LEXEME: '{token_lexeme}' (Starts at: {start_line}:{start_col}, Ends at: {end_line}:{end_col})")
#     print(repr(f"TYPE: {type_name:<15} LEXEME: '{token_lexeme}' (Starts at: {start_line}:{start_col}, Ends at: {end_line}:{end_col})"))
#     # repr() is needed because of the newline character
#     # couldn't make rf-string work
# 
# print(ast.dump(syntax_tree, indent=2))

# from ast import dump, parse, unparse
# 
# code_snippet = """y = 5
# x = 10 + y"""
# 
# syntax_tree = parse(code_snippet)
# unparsed_code = unparse(syntax_tree)
# reparsed_code = parse(unparsed_code)
# 
# print("-------------------------")
# print(f"Syntax Tree:\n{dump(syntax_tree, indent=2)}",sep='')
# print("-------------------------")
# print(f"Unparsed Code:\n{unparsed_code}",sep='')
# print("-------------------------")
# print(f"Reparsed Code:\n{dump(reparsed_code, indent=2)}",sep='')
# print("-------------------------")

# -----------------------------------------------------------------------------
# Week 8 - Functions Part 2

# def square(x):
#     return x*x
# 
# num_list = [1, 2, 3, 4, 5]
# 
# squared_map = map(square, num_list)
# 
# squared_list = list(squared_map)
# # Changing the type of the object from `map` to `list`, so it's human-readable.
# 
# print(squared_list)  # Output: [1, 4, 9, 16, 25]

# def is_even(x):
#     return x % 2 == 0
# 
# num_list = [i for i in range(20)]
# 
# evens_filter = filter(is_even, num_list)
# 
# evens = list(evens_filter)
# 
# print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# def factorial(num): return 1 if num == 0 else num * factorial(num-1)

# def factorial(num):
#     if num==0:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(5))


# class Vehicle:
#     def __init__(self, current_speed):
#         self.current_speed = current_speed
# 
#     def accelerate(self, speed):
#         self.current_speed += speed
#         print(self.current_speed)
# 
# class Bike(Vehicle):
#     def accelerate(self, speed):
#         self.current_speed += 2 * speed  # because bikes are cool
#         print(self.current_speed)
# 
# class Car(Vehicle):
#     def accelerate(self, speed):
#         self.current_speed += 0.5 * speed  # because cars are shit
#         print(self.current_speed)
# 
# class Truck(Vehicle):
#     def __init__(self):
#         self.current_speed = 0
# 
# my_bike = Bike(0)
# my_car = Car(0)
# my_truck = Truck()
# 
# my_bike.accelerate(10)  # Output: 20
# my_car.accelerate(10)  # Output: 5
# my_truck.accelerate(10)  # Output: 10
#
# from getpass import getpass
# from os import system
# # from time import sleep
#
# password = None
# mode = None
#
# while True:
#     system("clear")
#     print(
#         "|-------------------------------------------|\n",
#         "|       Completely-Secure-Interface         |\n",
#         "|-------------------------------------------|\n",
#         "| Enter Mode : 1                            |\n",
#         "| Set Mode   : 0                            |\n",
#         "|-------------------------------------------|",
#         sep='')
#     if password is None:
#         print(
#             "|-------------------------------------------|\n",
#             "| Set a password to use this interface.     |\n",
#             "|-------------------------------------------|",
#         sep='')
#         mode = 0
#     else:
#         print(
#             "|-------------------------------------------|\n",
#             "| Enter/Set :                               |\n",
#             "|-------------------------------------------|",
#         sep='')
#         mode = input()
#
#     try:
#         mode = int(mode)
#     except ValueError:
#         system("clear")
#         print(
#             f"|-------------------------------------------|\n",
#             f"| You've entered an invalid input           |\n",
#             f"| ('{mode}'), please try again.             |\n",
#             f"|-------------------------------------------|",
#         sep='')
#         continue
#
#     if mode == 1 and password is not None:
#         system("clear")
#         print(
#             "|-------------------------------------------|\n",
#             "| Please enter your password:               |\n",
#             "|-------------------------------------------|",
#         sep='')
#         pwd_try = getpass(" ")
#         if pwd_try == password:
#             system("clear")
#             print(
#                 "|-------------------------------------------|\n",
#                 "| Password is correct.                      |\n",
#                 "|-------------------------------------------|",
#             sep='')
#             break
#         else:
#             system("clear")
#             print(
#                 "|-------------------------------------------|\n",
#                 "| Incorrect password, please try again.     |\n",
#                 "|-------------------------------------------|",
#             sep='')
#             continue
#     elif mode == 0:
#         print(
#             "|-------------------------------------------|\n",
#             "| Please enter your new password:           |\n",
#             "|-------------------------------------------|",
#         sep='')
#         password = getpass(" ")
#         continue

# def lower_name(name):
#     return name.lower()
# 
# def clear_whitespace(dirtyString):
#     cleanString = ""
#     for c in dirtyString:
#         if not c.isspace():
#             cleanString += c
#     return cleanString
# 
# withWhitespace = "|     JAYSHOZIE   |"
# withoutWhitespace = clear_whitespace(withWhitespace)
# print(withoutWhitespace)

from time import sleep
def calculate_nums():
    x = 0
    y = 1
    print(0)
    while True:
        z = x + y
        x = y
        y = z
        print(z)
        sleep(0.25)

calculate_nums()
