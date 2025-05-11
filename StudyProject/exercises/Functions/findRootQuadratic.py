import math
def findRootQuadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    equation = "-------------\nf(x) = " + str(a) + "x^2 + " + str(b)+ "x + " + str(c)
    if a == 0:
        print(equation)
        print("-------------\nNot a qudaratic equation.\n")
    elif discriminant < 0:
        print(equation)
        print("-------------\nNo real roots.")
    elif discriminant == 0:
        x = (-b) / (2*a)    
        print(equation)
        print("-------------\nDouble Root: ", x)
    elif discriminant > 0:
        x1 = ((-b) + math.sqrt(discriminant))/(2*a)
        x2 = ((-b) - math.sqrt(discriminant))/(2*a)
        print(equation)
        print("-------------\nTwo Roots\n-------------\nx1 = ", x1, "\nx2 = ", x2)

# findRootQuadratic(1,0,0)
# findRootQuadratic(1,4,2)
# findRootQuadratic(0,2,3)
# findRootQuadratic(6,1,3)