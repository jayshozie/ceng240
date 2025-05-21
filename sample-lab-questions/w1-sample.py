# Week 1 Sample Questions and Solutions

"""
Question 1:

In this task, you will help a farmer who wants to calculate the area of a
rectangular field. Inputs will be given as floats in the followin order:
    * Length of the field (in meters)
    * Width of the field (in meters)

You must calculate the area in decares and print the result as float with 2
digits after the decimal point.

Hint: 1 sq. meters = 0.001 decares

Important Note: In order not to lose any points redundantly, you must NOT use
any argument for the `input()` function and comply with the output format.

Sample I/O:
----------

Input:
10
20

Output:
0.20


Input:
12.3
45.6

Output:
0.56
"""

# Sample Solution
L=float(input())
W=float(input())
A=L*W*0.001
print("{:.2f}".format(A))

"""
I hate this solution. As if it was designed to confuse people who just started
coding.
"""

# My Solution

# As it was said in the question, first we need to take the length of the
# field, which we will do with the `input()` function.

# What does this mean?
length = float(input())
# This line means that we are taking a command line input from the person who
# ran this python file. After taking the input, as it can be seen, we convert
# it into a floating point number with the function `float()`, because the
# question said so.

# After this we need to take the width of the field just like the previous line
width = float(input())

# Now we calculate the area of the field in sq. meters.
area = length * width

# However the question explicitly tells us that the output should be in decares
# , thus we convert it into decares using the formula given.

# How does this line work?
area = area * 0.001
# In almost every programming language you can re-assign a variable to itself
# This line takes the stored value of the variable `area` and then multiplies
# it with the floating point number `0.001`, then stores it in the same place.

# If the line area=area*0.001 confuses you, no problem.
# You can use this instead:
# area_in_decares = area * 0.001

# This is actually even better in some cases, since you still may need the area
# in sq. meters.

# Then we print the result with the given format
print("{:.2f}".format(area))
# You don't need to know what that line means entirely at this point.
# Just know that to print something on the command line you can use the
# function `print()`.

"""
Question 2:

Sphere in a Cube
----------------
You are given a sphere that perfectly fits inside a cube such that the diameter
of the sphere is equal to the edge length of the cube.

Write a program that calculates the absolute difference between the volume of
the cobue and the sphere. You should take the diameter of the sphere from the
user as a `float` and print the result as a `float` with 2 digits after the
decimal point.

Regulations & Hints:
--------------------
* You should take pi = 3.14 while calculating the volume of the sphere.
* You can use the following line to print you result in proper format:
    print('%.2f' % your_result)
* You should NOT print anything other than the result. Otherwise, your code
    will be graded as ZERO. Please verify your outputwith the sample given
    below. (Neither the string "Input:" nor "Output:" will be printed. You will
    only print a single floating point number which is the volume difference.)

Sample I/O:
-----------

Input:
5.5

Output:
79.31


Input:
10.0

Output:
476.67
"""

# Sample Solution

diameter = float(input())
volume_of_sphere = float(4/3*3.14*(diameter/2)**3)
volume_of_cube = float(diameter**3)
result = float(volume_of_cube - volume_of_sphere)
print('%.2f' % result)

"""
Sadly, same thing applies to this solution.
"""

# My Solution

"""
As the question states, we need to take only a single input, which is the
diameter of the sphere, which is also the side length of the cube
"""
pi = 3.14
diameter = float(input())
# If you don't know what this means, please check the previous question.

v_sphere = (4/3) * pi * (diameter/2)**3
# What the `**` operator?
# It is the power operator, it raises the left-hand side item to the right-hand
# side power. It's basically diameter * diameter * diameter.

"""
Why didn't I use the `float()` function here?
Because since the value of pi is already a float, and the same thing will
apply to the diameter, there is no need to use that function here.

Is this the most optimal?
There is only a single case in which this program may fail, which is if the
user enters a complex number. I don't think they will.
"""
v_cube = diameter**3
# Same thing applies here.

result = v_cube - v_sphere
# Again, no need to convert it to float, they are all floats anyway.

print('%.2f' % result)


# If you have any questions please don't hesitate to reach out.
# You can open up an issue, if you didn't understand something in this file.
