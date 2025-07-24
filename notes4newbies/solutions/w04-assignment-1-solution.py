











import math

nums = eval(input("Enter 5 numbers in a list (e.g. [10, 20, 30, 40, 50]) : "))

largest = (-1) * math.inf
smallest = math.inf

total = 0
for i in nums:
    if i <= smallest:
        smallest = i
    if i >= largest:
        largest = i

    total += i


mean = total / len(nums)

if len(nums) % 2 == 0:
    median = nums[len(nums)/2]
else:
    math.
    lower_mid = len(nums)/2
    median =
















