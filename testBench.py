total = 0

while True:
    print(f"Total : {total}")
    num = eval(input("New Num : "))

    if isinstance(num, (int,float)):
        total += num
    else:
        continue

    if num <= 0:
        print(f"Total : {total}")
        print(f"Done.")
        break
