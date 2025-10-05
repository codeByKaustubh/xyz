#Implement the A Search algorithm for solving a pathfinding problem.
import heapq

graph = {
    "S": [("A", 2), ("B", 4)],
    "A": [("S", 2), ("B", 2), ("C", 3), ("D", 7)],
    "B": [("S", 4), ("A", 2), ("C", 1)],
    "C": [("A", 3), ("B", 1), ("G", 5)],
    "D": [("A", 7), ("G", 2)],
    "G": [("C", 5), ("D", 2)]
}
heuristic = {
    "S": 7, "A": 6, "B": 2, "C": 1, "D": 1, "G": 0
}
def astar(start, goal):
    pq = [(heuristic[start], 0, start, [start])]  # (f = g + h, g, node, path)
    visited = set()
    
    while pq:
        f, g, node, path = heapq.heappop(pq)
    
        if node == goal:
            return path, g
        
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float("inf")

path, cost = astar("S", "G")
print("A* Path:", path, "Cost:", cost)