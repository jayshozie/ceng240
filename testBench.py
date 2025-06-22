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

def is_even(x):
    return x % 2 == 0

num_list = [i for i in range(20)]

evens_filter = filter(is_even, num_list)

evens = list(evens_filter)

print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
