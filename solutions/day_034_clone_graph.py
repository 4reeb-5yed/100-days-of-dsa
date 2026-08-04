class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):
    if not node:
        return None
    clone_map = {}
    
    def dfs(n):
        if n in clone_map:
            return clone_map[n]
        clone = Node(n.val)
        clone_map[n] = clone
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone
    
    return dfs(node)