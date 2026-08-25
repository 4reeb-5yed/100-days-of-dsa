from collections import deque

def right_side_view(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node[0])
            if len(node) > 1 and node[1]:
                queue.append(node[1])
            if len(node) > 2 and node[2]:
                queue.append(node[2])
    return result