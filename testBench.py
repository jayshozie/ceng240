# Bubble Sort

from random import randint
unsorted = [randint(-1000, 1000) for _ in range(10)]

# unsorted = eval(input("Please enter the unsorted list : "))

for i in range(len(unsorted)-1):
    for i in range(len(unsorted)-1):
        if unsorted[i] > unsorted[i+1]:
            tmp = unsorted[i+1]
            unsorted[i+1] = unsorted[i]
            unsorted[i] = tmp

print(f"Sorted List : {unsorted}")
