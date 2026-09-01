def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True
        if isinstance(node, int):
            return low < node < high
        if node[0] <= low or node[0] >= high:
            return False
        left_valid = validate(node[1], low, node[0]) if len(node) > 1 and node[1] else True
        right_valid = validate(node[2], node[0], high) if len(node) > 2 and node[2] else True
        return left_valid and right_valid
    return validate(root, float('-inf'), float('inf'))