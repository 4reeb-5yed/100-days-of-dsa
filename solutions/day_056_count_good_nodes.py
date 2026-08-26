def count_good_nodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        is_good = 1 if node[0] >= max_val else 0
        new_max = max(max_val, node[0])
        left = dfs(node[1], new_max) if len(node) > 1 and node[1] else 0
        right = dfs(node[2], new_max) if len(node) > 2 and node[2] else 0
        return is_good + left + right
    return dfs(root, float('-inf'))