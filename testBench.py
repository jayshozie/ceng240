coordinate = eval(input())

if (coordinate[0] == 0 or
    coordinate[1] == 0):

    if coordinate[0] == 0 and coordinate[1] > 0:
        print(f"{coordinate} is between quadrant I and II.")
    elif coordinate[0] == 0 and coordinate[1] < 0:
        print(f"{coordinate} is between quadrant III and IV.")
    elif coordinate[0] > 0 and coordinate[1] == 0:
        print(f"{coordinate} is between quadrant I and IV.")
    elif coordinate[0] < 0 and coordinate[1] == 0:
        print(f"{coordinate} is between quadrant II and III.")
    elif coordinate[0] == 0 and coordinate[1] == 0:
        print(f"{coordinate} is the origin")

else:
    if coordinate[0] > 0 and coordinate[1] > 0:
        print(f"{coordinate} is in quadrant I.")
    elif coordinate[0] < 0 and coordinate[1] > 0:
        print(f"{coordinate} is in quadrant II.")
    elif coordinate[0] < 0 and coordinate[1] < 0:
        print(f"{coordinate} is in quadrant III.")
    elif coordinate[0] > 0 and coordinate[1] < 0:
        print(f"{coordinate} is in quadrant IV.")
