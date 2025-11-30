def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input(f"Node {i+1}: ").strip()
        neighbors = input(f"Neighbors of {node} (comma-separated): ").strip()
        graph[node] = [x.strip() for x in neighbors.split(",")] if neighbors else []
    return graph


def dfs(graph, node, goal, visited, path):
    visited.append(node)
    path.append(node)

    if node == goal:
        return True  # goal found

    for nei in graph.get(node, []):
        if nei not in visited:
            if dfs(graph, nei, goal, visited, path):
                return True

    path.pop()   # backtrack
    return False


# Main
graph = input_graph()
start = input("Start node: ").strip()
goal = input("Goal node: ").strip()

visited = []
path = []

found = dfs(graph, start, goal, visited, path)

print("\n=== DFS (Recursive) ===")
print("Visited:", visited)
print("Path:", " -> ".join(path) if found else "No path found")
