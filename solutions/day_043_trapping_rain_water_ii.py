import heapq

def trap_rain_water(height_map):
    if not height_map or not height_map[0]:
        return 0
    m, n = len(height_map), len(height_map[0])
    visited = [[False] * n for _ in range(m)]
    heap = []
    
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(heap, (height_map[i][j], i, j))
                visited[i][j] = True
    
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    water = 0
    
    while heap:
        height, r, c = heapq.heappop(heap)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                if height_map[nr][nc] < height:
                    water += height - height_map[nr][nc]
                heapq.heappush(heap, (max(height, height_map[nr][nc]), nr, nc))
    return water