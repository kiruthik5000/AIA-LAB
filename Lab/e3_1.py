def a_star(graph, h, start, end):

    open_list = [start, [start], 0] # queue for bfs contains [curNode, path, curDist]

    visited = set()

    # bfs
    while open_list:
        open_list.sort(key=lambda x: x[2] + h[x[0]])
        curNode, path, dist = open_list.pop(0)

        print("Visiting: ", curNode)

        if curNode == end:
            print("\n Goal Reached")
            return path

        for neighbour, edge_cost in graph.get(curNode, []):
            if neighbour not in visited:
                total_cost = dist + edge_cost
                open_list.append((neighbour, path + [neighbour], total_cost))
    print("\n No Path Found")
    return None

# ------------ Input ------------
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

result = a_star(graph, h, start, end)

if result:
    print("Path: ", "->".join(result))
else:
    print("Cannot reach goal")

