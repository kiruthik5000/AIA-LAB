def greedy_best_first_search(graph, h, start, goal):
    print("\nGreedy Best-First Search")

    open_list = [(start, [start])]
    visited = set()

    while open_list:
        # Sort by heuristic value (smallest first)
        open_list.sort(key=lambda x: h[x[0]])

        current, path = open_list.pop(0)
        print("Visiting:", current)

        if current == goal:
            print("\nGoal Reached!")
            return path

        visited.add(current)

        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor]))

    print("\nNo Path Found.")
    return None


# ---- INPUT SECTION ----
graph = {}

n = int(input("Enter Number of Nodes: "))

for _ in range(n):
    curNode = input("Enter Current Node: ")
    neighbours = input("Enter the neighbours of the Node eg: B 1, D 2")
    neighbour_list = []

    if neighbours:
        for pair in neighbours.strip().split(','):
            child, cost = pair.strip().split(" ")

            neighbour_list.append((child, cost))
    graph[curNode] = neighbour_list

h = {}

for node in graph:
    h[node] = int(input(f"Enter the herustic value of Node {node}: "))

start = input("Enter the start Node: ")
end = input("Enter the end Node: ")

result = greedy_best_first_search(graph, h, start, end)

if result:
    print("Path: ", "->".join(result))
else:
    print("Cannot reach goal")