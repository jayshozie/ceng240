








from math import pi

radius_1 = eval(input())
radius_2 = eval(input())

area_1 = pi * radius_1**2
area_2 = pi * radius_2**2

area_diff = abs(area_1 - area_2)

if area_diff != 0:
    if radius_1 > radius_2:
        print(f"{radius_1} > {radius_2}")
        print(f"Area Difference : {area_diff}")

    elif radius_1 < radius_2:
        print(f"{radius_2} > {radius_1}")
        print(f"Area Difference : {area_diff}")

    else:
        print("A problem has ocurred.")

elif area_diff == 0:
    print(f"{radius_1} = {radius_2}")
    print(f"Area Difference : {area_diff}")
