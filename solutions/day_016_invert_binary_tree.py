def invert_tree(root):
    if root is None or isinstance(root, int):
        return root
    if len(root) <= 1:
        return root
    root[1], root[2] = (invert_tree(root[2]) if len(root) > 2 and root[2] else None), (invert_tree(root[1]) if len(root) > 1 and root[1] else None)
    return root