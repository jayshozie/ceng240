num = eval(input("Please enter a numerical value: "))

if num % 2 == 0:
    print(f"{num} is even.")
elif num % 2 == 1:
    print(f"{num} is odd.")
else:
    print(f"{num} is neither even nor odd.")
