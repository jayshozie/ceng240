age = eval(input("Please enter your age: "))

if isinstance(age, (int, float)):
    if age >= 18:
        print(f"You are {age} years old. You're a legal adult.")
    else:
        print(f"You are {age} years old. You're not a legal adult.")
else:
    print(f"You've entered {age} as your age. Please enter a valid number.")
