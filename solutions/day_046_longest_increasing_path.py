def longest_increasing_path(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    
    def dfs(r, c):
        if dp[r][c]:
            return dp[r][c]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_path = 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                max_path = max(max_path, 1 + dfs(nr, nc))
        dp[r][c] = max_path
        return max_path
    
    return max(dfs(r, c) for r in range(m) for c in range(n))