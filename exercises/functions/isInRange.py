def isInRange(value, range_given):
    """
    A function that checks whether a certain value is in a given range.

    Arguments
    ---------
    value : int, float
        Value that needs to be checked.
    range_given : tuple, range, list
        Given range the function will check whether the value is in.
    """
    if not isinstance(value, (int, float)): 
        raise TypeError("Range must be int or float.")
    elif not isinstance(range_given, (tuple, range, list)):
        raise TypeError("Range must be int or float.")
    if type(range_given) == range:
        if value in range_given:
            return True
        else:
            return False 
    elif type(range_given) == tuple or type(range_given) == list:
        if len(range_given) < 2 or len(range_given) > 2:
            raise ValueError("Range cannot have less than or more than 2 values.")
        else:
            tmpLower, tmpUpper = range_given[0], range_given[1]
            if tmpLower <= value <= tmpUpper:
                return True
            else:
                return False
    else:
        raise TypeError("Range must be either a range or a list or tuple with only 2 numbers in.")
        
# print(isInRange(5, [8, 10]))