in_list = eval(input())

for item in range(len(in_list)):
    if type(in_list[item]) == list:
        avg = sum(in_list[item]) / len(in_list[item])
        in_list[item] = avg

print(in_list)
