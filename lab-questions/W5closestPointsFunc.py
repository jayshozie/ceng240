def man(p1,p2):
    return abs(p1[1]-p2[1]) + abs(p1[0]-p2[0])

def closest_points(points): # Takes in a list of tuples, representing coordinates in a 2D plane. Returns the closest, according to manhattan distance.
    closest = []
    shortest = float('inf')
    outer = 0
    for p1 in points:
        inner = 0
        for p2 in points:
            distance = man(p1,p2)
            if inner <= outer:
                inner += 1
                continue
            elif distance < shortest:
                shortest = distance
                closest = [p1,p2]
                inner += 1
        outer += 1
    return closest

print(closest_points([(1,2),(3,4),(9,14),(8,27)]))
print(closest_points([(2,2),(3,2),(2,4),(2,2)]))
print(closest_points([(0,0),(0,1)]))
print(closest_points([(0,0),(0,10),(100,100),(100,101)]))
