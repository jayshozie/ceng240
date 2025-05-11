"""
Week 4 Sample Question and Solution

Question 1:
You are expected to implement a function that checks a list of chemical
elements and determines whether each of them is dangerous or not. The function
definition and its parameters are as follows:

check_list(NameOfChemical, XFactorList, YFactorList, ZFactorList)
    - NameOfChemical: A list of strings.
    - XFactorList: A list of floats.
    - YFactorList: A list of floats.
    - ZFactorList: A list of floats.

Every chemical element has a score which you can calcuulate with this formula:
(XFactor / YFactor-1) * ZFactor. If it is greater than 1 then the element is
dangerous, if it is less than or equal to 1, then it is not dangerous.

The function should return a list:
    - The list should contain the names of the elements and their
        classification, whether the element is dangerous or not. The element
        name should be followe dby a 'D' if the element is dangerous, otherwise
        it should be followed by 'ND'.

Hints & Regulations:
- Your function shall receive its data via its parameters only. Your submetted
    solution will not use any input() function.
- Your function shall return its results. It will NOT print anything.
- Any return value that doesn't conform to the expected output type will be
    graded as zero.


Sample I/O:

Input:
>>> check_list(['Neon', 'Vanadium', 'Niobium', 'Chlorine'], [1.33, 1.85, 1.76,
1.26], [1.96, 1.95, 1.06, 1.08], [13, 28, 19, 31])
Output:
['Neon', 'ND', 'Vanadium', 'ND', 'Niobium', 'D', 'Chlorine', 'D']

Input:
>>> check_list(['fermium', Roentgenium', Zirconium', 'Vanadium', 'Copernicium']
, [1.96, 1.95, 1.06, 1.08, 1.84], [1.24, 1.54, 1.37, 1.16, 1.63], [13, 6, 20, 9
, 4])
Output:
['fermium', 'ND', 'Roentgenium', 'D', 'Zirconium', 'ND', 'Vanadium', 'ND',
'Copernicium', 'ND']

To help you understand the question better, you can follow the execution steps
of the second example input/output combination which you can find below:
    - First chemical Fermium, its XFactor is 1.96, YFactor is 1.24 and ZFactor
        is 13. If you put these scores into the formula which is (XFactor /
        YFactor-1) * ZFactor = (1.96/1.24-1) * 13 = 7.5483 so it is greater
        than 1, it is dagnerous.
    - Put Roentgenium into the formula:
        (1.95/1.54-1) * 6 = 1.5974 so it is greater than 1, it is dangerous.
    - Put Zirconium into the formula:
        (1.06/1.37-1) * 20 = 4.525 so it is lower than 1, it is not dangerous.
    - Put Vanadium into the formula:
        (1.08/1.16-1) * 9 = 0.5153 so it is lower than 1, it is not dangerous.
    - Returned list should be ['Fermium', 'D', 'Roentgenium', 'D', 'Zirconium',
        'ND', 'Vanadium', 'ND', 'Copernicium', 'ND'] because Zirconium,
        Vanadium and Copernicium are not dangerous, rest of them are dangerous.
"""

# Solution


def check_list(NameOfChemical, XFactorList, YFactorList, ZFactorList):
    result = []
    for i in range(len(NameOfChemical)):
        score = (XFactorList[i] / YFactorList[i] - 1) * ZFactorList[i]
        if score > 1:
            result.append(NameOfChemical[i])
            result.append('D')
        else:
            result.append(NameOfChemical[i])
            result.append('ND')
    return result
