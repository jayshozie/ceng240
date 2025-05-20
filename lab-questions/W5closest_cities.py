# This is a Dijkstra's algorithm solution for CENG240 lab exam question
# Write a function that takes in 2 arguments: a list of tuples of cities
# and the distance between them, and a string of 2 cities.
# The function should return the shortest distance between the two cities.

def shortest(routes, cities):
    # Create a dictionary to store the distances between cities
    distances = {}
    for route in routes:
        city1, city2, distance = route
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}
        distances[city1][city2] = distance
        distances[city2][city1] = distance

    # Initialize the shortest distance to infinity
    shortest_distance = float('inf')

    # Split the input cities into two separate variables
    city1, city2 = cities.split('-')

    # Check if the two cities are directly connected
    if city1 in distances and city2 in distances[city1]:
        return distances[city1][city2]

    # Initialize a list to keep track of visited cities
    visited = []

    # Initialize a queue for BFS
    queue = [(city1, 0)]

    while queue:
        current_city, current_distance = queue.pop(0)

        # If we reach the destination city, update the shortest distance
        if current_city == city2:
            shortest_distance = min(shortest_distance, current_distance)
            continue

        # Mark the current city as visited
        visited.append(current_city)

        # Explore neighboring cities
        for neighbor, distance in distances.get(current_city, {}).items():
            if neighbor not in visited:
                queue.append((neighbor, current_distance + distance))

    return shortest_distance if shortest_distance != float('inf') else -1  # Return -1 if no path found

# Test cases
print(shortest([('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 2)], 'A-B'))  # Output: 1
print(shortest([('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 2)], 'A-C'))  # Output: 2
