num = eval(input("Factorial of (must be an integer)? : "))
counter = 1
output = 1

if num == 0:
    print(f"0! = 1")
else:
    for i in range(num):
        output *= counter
        counter += 1

    print(f"{num}! = {output}")
