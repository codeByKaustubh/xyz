#Implement the Breadth First Search algorithm to solve a given problem.
from collections import deque

graph = {
    "S": [("A", 2), ("B", 4)],
    "A": [("S", 2), ("B", 2), ("C", 3), ("D", 7)],
    "B": [("S", 4), ("A", 2), ("C", 1)],
    "C": [("A", 3), ("B", 1), ("G", 5)],
    "D": [("A", 7), ("G", 2)],
    "G": [("C", 5), ("D", 2)]
}

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    
    return None

print("BFS Path:", bfs("S", "G"))