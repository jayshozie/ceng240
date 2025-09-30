import math

nums = eval(input("Enter 5 numbers in a list (e.g. [10, 20, 30, 40, 50]) : "))

# assuming the list is ordered
largest = nums[-1]
smallest = nums[0]

# calculating the mean value
total = 0
for i in nums:
    total += i
mean = total / len(nums)

# or you can use
# mean = sum(nums) / len(nums)

print(f"""
Largest  : {largest}
Smallest : {smallest}
Mean     : {mean}
""")
