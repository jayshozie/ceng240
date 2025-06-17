def f(List):
    List = List[::-1]

def g():
    L = [1, 2, 3]
    print(L)

    f(L)
    print(L)

g()
# Output:
# [1, 2, 3]
# [1, 2, 3]
