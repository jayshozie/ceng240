# Week 4 Sample Question and Solution

"""
Question:

You are expected to implement a function that checks a list of chemical
elements and determines whether each of them is dangerous or not. The function
definition and its parameters are as follows:

check_list(NamesOfChemicals, XFactorList, YFactorList, ZFactorList)
* NamesOfChemicals : A list of strings
* XFactorList : A list of floats
* YFactorList : A list of floats
* ZFactorList : A list of floats

Every chemical element has a score which you can calculate with this formula:
    (XFactor/YFactor-1)*ZFactor
If this is greater than 1 then the element is considered dangerous, if it is
less than or equal to 1, then it's not considered dangerous.

The function should return a list:
* The list should contain the names of the elements and their classification,
    whether the element is dangerous or not. The element name should be
    followed by a 'D' if the element is dangerous, otherwise it should be
    followed by an 'ND'.

Hints & Regulations:
--------------------
* Your function shall receive its data via its parameters only. Your submitted
    solution will not use any `input()` function.
* Your function shall return its results. It will NOT print anything.
* Any return value that doesn't conform to the expected output type will be
    graded as zero.

Sample I/O:
-----------

>>> check_list(['Neon', 'Vanadium', 'Niobium', 'Chlorine'], [1.13, 1.85, 1.76,
1.26], [1.96, 1.95, 1.06, 1.08], [13, 28, 19, 31])
['Neon', 'ND', 'Vanadium', 'ND', 'Niobium', 'D', 'Chlorine', 'D']

Note that the output is not printed by the `check_list()` function. It is the
read-eval-print_result looping of the Python interpreter that did the printing
of the list value, returned by the function.

>>> check_list(['Fermium', 'Roentgenium', 'Zirconium', 'Vanadium',
'Copernicium'], [1.96, 1.95, 1.06, 1.08, 1.84], [1.24, 1.54, 1.37, 1.6, 1.63],
[13, 6, 20, 9, 4])
['Fermium', 'D', 'Roentgenium', 'D', 'Zirconium', 'ND', 'Vanadium', 'ND',
'Copernicium', 'ND']


To help you understand the question better, you can follow the execution steps
of the second example I/O combination which you can find below:

* First chemical Fermium, its XFactor is 1.96, its YFactor is 1.24, and its
    ZFactor is 13. If you put these score sinto the formula which is
    (XFactor/YFactor-1)*ZFactor
        - (1.96/1.24-1)*13 = 7.5483 so it is greater than 1, dangerous.
* Put Roentgenium values into the formula:
    (1.95/1.54-1)*6 = 1.5974 so it is greater than 1, dangerous.
* Zirconium:
    (1.06/1.37-1)*20 = -4.525, lower than 1, not dangerous.
* Vanadium:
    (1.08/1.6-1)*9 = -2.925, lower than 1, not dangerous.
* Copernicium:
    (184/1.63-1)*4 = 0.5153, lower than 1, not dangerous.
* Returned list should be ['Fermium', 'D', 'Roentgenium', 'D', 'Zirconium',
    'ND', 'Vanadium', 'ND', 'Copernicium', 'ND'] because Zirconium, Vanadium
    and Copernicium are not dangerous, rest of them are dangerous.
"""

# Sample Solution


def check_list(NamesOfChemicals, XFactorList, YFactorList, ZFactorList):
    main_list = []

    for i in range(len(NamesOfChemicals)):
        if ((XFactorList[i]/YFactorList[i]-1)*ZFactorList[i]) > 1:
            main_list.append(NamesOfChemicals[i])
            main_list.append('D')
        else:
            main_list.append(NamesOfChemicals[i])
            main_list.append('ND')

    return main_list


"""
This solution is good, but it could be easier to read and replicate.
"""

# My Solution


def my_check_list(NamesOfChemicals, XFactorList, YFactorList, ZFactorList):
    ret_list = []

    for i in range(len(NamesOfChemicals)):
        score = ((XFactorList[i] / YFactorList[i] - 1) * ZFactorList[i])

        ret_list.append(NamesOfChemicals[i])
        if score > 1:
            ret_list.append('D')
        else:  # score <= 1
            ret_list.append('ND')

    return ret_list


"""
Explanation
-----------

If you set a variable called score, and write the formula for it before the
check it is easier to change, see, and understand the formula.

There is no case in which we're not appending the name of the chemical to our
return list, so just append it before the score check, so that you don't need
to write it in both if-cases.
"""


# If you have any questions please don't hesitate to reach out.
# You can open up an issue, if you didn't understand something in this file.
