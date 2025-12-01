def a_star(graph, h, start, end):
    q = [(start, [start], 0)]
    visited = set()
    while q:
        q.sort(key=lambda x: x[2] + h[x[0]])
        cur, path, curDist = q.pop(0)

        print(f"visiting: {cur}")

        if cur == end:
            print("Goal Reahed\n")
            return path
        visited.add(cur)

        for child, edge_cost in graph.get(cur, []):
            if child not in visited:
                q.append((child, path + [child], curDist + edge_cost))
    print("No path found")
    return None

graph = {}
n = int(input("Enter number of nodes"))
for i in range(n):
    node = input("Enter name of the node: ")
    neighbours = input("Enter the neighbours name, dist")
    neighbours_list = []

    for pair in neighbours.split(','):
        node, dist = pair.split(' ')
        neighbours_list.append((node, int(dist)))
    graph[node] = neighbours_list

h = {}
for node in graph:
    h[node] = int(input(f'Enter h val of node {node}'))

start = input('enter start node')
end = input('enter end node')

result = a_star(graph, h, start, end)

if result:
    print("->".join(result))
else:
    print("No path found")

