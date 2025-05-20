# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

"""
A triplet is 3 numbers in row that satisfies these 3 conditions:
1. The first number is less than the second number.
2. Second number should be divisible by 2.
3. The third number should be the sum of the first two numbers.

Write a function that takes a list of numbers and counts the amount of triplets in the list.

Example:
Input: [1, 2, 3, 4, 6, 10, 5, 8, 13]
Output: 3
"""

def tripletCounter(nList): # Takes in a list of numbers. Returns the total number of triplets in it.
    count = 0
    for i in range(len(nList)-2): # Iteration. -2 is for error handling.
        if (nList[i] < nList[i+1] and
            nList[i+1]%2 == 0 and
            nList[i+2] == nList[i] + nList[i+1]):
            # Conditions of being a triplet.
            count += 1
    return count
