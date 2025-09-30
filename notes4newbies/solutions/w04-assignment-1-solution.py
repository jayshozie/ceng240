# Solution of Assignment 1


# Solution of Assignment 2

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

# Solution of Assignment 2 Harder Version

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


n = len(nums)
s = sorted(nums)
if n:
    median = (s[n//2-1]/2.0 + s[n//2]/2.0, s[n//2])[n % 2]
else:
    median = None

# or more explicitly:
# sortedLst = sorted(nums)
# lstLen = len(nums)
# index = (lstLen - 1) // 2
#
# if (lstLen % 2):
#     return sortedLst[index]
# else:
#     return (sortedLst[index] + sortedLst[index + 1])/2.0

# or using a library:
# from numpy import median
# s = nums.sort()
# median = median(s)

print(f"""
Largest  : {largest}
Smallest : {smallest}
Mean     : {mean}
Median   : {median}
""")















