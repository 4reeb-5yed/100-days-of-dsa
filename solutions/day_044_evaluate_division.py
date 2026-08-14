def calc_equation(equations, values, queries):
    graph = {}
    for (a, b), val in zip(equations, values):
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = val
        graph[b][a] = 1 / val
    
    def dfs(a, b, visited):
        if a not in graph or b not in graph:
            return -1.0
        if b in graph[a]:
            return graph[a][b]
        for neighbor in graph[a]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, b, visited)
                if result != -1.0:
                    return result * graph[a][neighbor]
        return -1.0
    
    return [dfs(a, b, {a}) for a, b in queries]