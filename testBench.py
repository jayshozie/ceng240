def f(n):
    n = n + 20

def g():
    a = 20
    print(a)
    f(a)
    print(a)

g()
# Output: 
# 20
# 20

# Why?
# Explanation:
# In the function `g`, the variable `a` is defined with a value of 20.
# When `f(a)` is called, it passes the value of `a` (which is 20) to the
# function `f`. Inside `f`, the parameter `n` receives this value, and then `n`
# is modified by adding 20 to it. However, this modification does not affect
# the variable `a` in the function `g`, because integers are immutable in
# Python.
