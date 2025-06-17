in_list = eval(input("Please enter the list you want to optimize : "))

for item in in_list:
    if type(item) == list:
        avg = sum(item) / len(item)
        in_list[in_list.index(item)] = avg

print(in_list)
