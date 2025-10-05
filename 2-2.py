#Implement the Recursive Best-First Search algorithm for the same problem.
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

def rbfs(node, path, g, f_limit, goal):
    print(f"Visiting {node} | g={g} | f_limit={f_limit} | path={path}")  # Debug line

    if node == goal:
        return path, g

    successors = []
    for neighbor, cost in graph[node]:
        if neighbor in path:  # Avoid cycles
            continue
        new_g = g + cost
        f = new_g + heuristic[neighbor]
        successors.append([f, neighbor, path + [neighbor], new_g])

    if not successors:
        return None, float("inf")

    while True:
        # Sort successors by f-value
        successors.sort(key=lambda x: x[0])
        best = successors[0]

        # If best f-value exceeds the limit, return failure and new limit
        if best[0] > f_limit:
            return None, best[0]

        # Find the second-best f for the alternative path
        alternative = successors[1][0] if len(successors) > 1 else float("inf")

        # Recursive call with new f_limit
        result, best_f = rbfs(best[1], best[2], best[3], min(f_limit, alternative), goal)
        best[0] = best_f
        successors[0] = best

        if result is not None:
            return result, best_f

# Run RBFS
path, cost = rbfs("S", ["S"], 0, float("inf"), "G")
print("\nRBFS Path:", path)
print("Total Cost:", cost)