def pacific_atlantic(heights):
    if not heights:
        return []
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]
    
    def dfs(r, c, ocean, prev_height):
        if r < 0 or c < 0 or r >= m or c >= n:
            return
        if ocean[r][c] or heights[r][c] < prev_height:
            return
        ocean[r][c] = True
        dfs(r + 1, c, ocean, heights[r][c])
        dfs(r - 1, c, ocean, heights[r][c])
        dfs(r, c + 1, ocean, heights[r][c])
        dfs(r, c - 1, ocean, heights[r][c])
    
    for c in range(n):
        dfs(0, c, pacific, heights[0][c])
        dfs(m - 1, c, atlantic, heights[m - 1][c])
    for r in range(m):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, n - 1, atlantic, heights[r][n - 1])
    
    result = []
    for r in range(m):
        for c in range(n):
            if pacific[r][c] and atlantic[r][c]:
                result.append([r, c])
    return result