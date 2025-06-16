upper_bound = eval(input("Please enter an upper bound: "))
num_list = []
counter = 1

for i in range(upper_bound):
    if counter**3 > upper_bound:
        break

    num_list.append(counter**3)
    counter += 1

print(f"Upper Bound : {upper_bound}")
print(f"Numbers : {num_list}")
