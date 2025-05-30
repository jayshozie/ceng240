# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

def isPrime(value):
    """
    Checks whether the given value is prime.

    Arguments
    ---------
    value : int, float
        Number that will be checked whether it is prime or not.

    Returns
    -------
    True
        If value is prime.
    False
        If value is not prime or the type of value is float.
    
    Raises
    ------
    TypeError
        If the type of value is not int or float.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be either int or float.")
    elif type(value) == float:
        return False
    elif value == 2:
        return True
    elif value % 2 == 0:
        return False
    else:
        halfOfValue = value/2
        i = 3
        while i < halfOfValue:
            if value % i == 0:
                return False
            else:
                i += 2
        return True

# print(isPrime())
