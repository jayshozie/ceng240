upper_limit = eval(input("Please enter an upper limit: "))
num_list = []
total = 0

if upper_limit > 0:
    for i in range(upper_limit):
        num_list.append(i+1)
        
total = sum(num_list)

print(f"Numbers : {num_list}")
print(f"Total : {total}")
