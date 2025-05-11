"""
Week 1 Sample Questions and Solutions

Question 1:

In this task you will help a farmer who wants to calculate the area of a
rectangular field.

Inputs will be given as floats in the following order.
1. Length of the field
2. Width of the field

You must calculate the area in decares and print the result as a float with 2
digits after the decimal point.

Hint: 1 square meter = 0.0001 decares

Important Note: In order not to lose any point redundantly, you must NOT use
any arguments for the input() function and comply with the output format.


Sample I/O:

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

# Solution

length = float(input())
width = float(input())
area = length * width * 0.0001
print(f"{area:.2f}")

"""
Question 2: Sphere in a Cube

You are given a sphere that perfectly fits inside a cube such that the diameter
of the sphere is equal to the edge length of the cube.

Write a program that calculates the absolute difference between the volume of
the cube and the sphere. You should take the diameter of the sphere from the
user as a float and print the result as a float with 2 digits after the decimal
point.

Regulations & Hints:
- You should take pi=3.14 while calculating the volume of the sphere.
- You can use the following line to print your result in proper format.
    print('%.2f' % your_result)
- You should NOT print anything other than the result. Otherwise, your code
    will be graded as ZERO. Please verify your output and confirm with the
    below given sample: (Neither the string "Input:" nor the string "Output:"
    should be printed. You will print only a single floating point which is the
    volume difference.)


Sample I/O:

Input:
5.5
Output:
79.31

Input:
10.0
Output:
476.67
"""

# Solution

diameter = float(input())
volume_sphere = float(4/3 * 3.14 * (diameter/2)**3)
volume_cube = diameter**3
result = abs(volume_cube - volume_sphere)
print('%.2f' % result)
