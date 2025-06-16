input_list = eval(input("Please enter 10 numbers, separated by commas (,): "))
sum = 0
for i in range(len(input_list)):
    sum += input_list[i]
mean = sum / 10

print(f"Sum : {sum}")
print(f"Average (mean) : {mean}")
