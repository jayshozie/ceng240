in_list = eval(input("Please enter the list : "))
item = int(input("Please enter the number you're searching for : "))
found = False

for i in range(len(in_list)):
    if in_list[i] == item:
        print("True")
        found = True

if found is False:
    print("False")
