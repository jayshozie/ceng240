lowercase_alphabeticals = [chr(i) for i in range(ord('a'), ord('z') + 1)]
uppercase_alphabeticals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lowercase_alphabeticals.extend(uppercase_alphabeticals)

alphabeticals = lowercase_alphabeticals.copy()

digits = [chr(i) for i in range(ord('0'), ord('9') + 1)]

input_char = str(input("Please enter a character: "))

if input_char in alphabeticals:
    print(f"{input_char} is an alphabetical character.")
elif input_char in digits:
    print(f"{input_char} is a digit character.")
else:
    print(f"{input_char} is a special character.")
