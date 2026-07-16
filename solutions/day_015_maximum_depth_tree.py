def max_depth(root):
    if root is None:
        return 0
    if isinstance(root, int):
        return 1
    left_depth = max_depth(root[1]) if len(root) > 1 and root[1] else 0
    right_depth = max_depth(root[2]) if len(root) > 2 and root[2] else 0
    return 1 + max(left_depth, right_depth)