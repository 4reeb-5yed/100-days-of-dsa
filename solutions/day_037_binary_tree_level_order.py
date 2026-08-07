from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node[0])
            if len(node) > 1 and node[1]:
                queue.append(node[1])
            if len(node) > 2 and node[2]:
                queue.append(node[2])
        result.append(level)
    return result