def find_circle_num(is_connected):
    n = len(is_connected)
    visited = [False] * n
    provinces = 0
    
    def dfs(city):
        visited[city] = True
        for neighbor in range(n):
            if is_connected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    for city in range(n):
        if not visited[city]:
            dfs(city)
            provinces += 1
    return provinces