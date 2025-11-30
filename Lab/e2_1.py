from collections import deque

def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input(f"Node {i+1}: ").strip()
        neighbors = input(f"Neighbors of {node} (comma-separated): ").strip()
        graph[node] = [x.strip() for x in neighbors.split(",")] if neighbors else []

    return graph

def bfs(graph, start, goal):
    
    visited = []
    # q of paths
    queue = deque([[start]])

    while queue:
    
    #   cur path [A, B, C]
        path = queue.popleft()
    # cur element [C]
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return visited, path

            for nei in graph.get(node, []):
                queue.append(path + [nei])

    return visited, []

# Main
graph = input_graph()
start = input("Start node: ").strip()
goal = input("Goal node: ").strip()

visited, path = bfs(graph, start, goal)

print("\n=== BFS ===")
print("Visited:", visited)
print("Path:", " -> ".join(path) if path else "No path found")
