def lowest_common_ancestor(root, p, q):
    if not root or root[0] == p or root[0] == q:
        return root[0]
    left = lowest_common_ancestor(root[1], p, q) if len(root) > 1 and root[1] else None
    right = lowest_common_ancestor(root[2], p, q) if len(root) > 2 and root[2] else None
    if left and right:
        return root[0]
    return left or right