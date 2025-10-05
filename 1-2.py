#Implement the Iterative Depth First Search algorithm to solve the same problem.
graph = {
    "S": [("A", 2), ("B", 4)],
    "A": [("S", 2), ("B", 2), ("C", 3), ("D", 7)],
    "B": [("S", 4), ("A", 2), ("C", 1)],
    "C": [("A", 3), ("B", 1), ("G", 5)],
    "D": [("A", 7), ("G", 2)],
    "G": [("C", 5), ("D", 2)]
}

def dfs_iter(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph[node]:
                stack.append((neighbor, path + [neighbor]))
    
    return None

print("DFS Iterative Path:", dfs_iter("S", "G"))
