def min_mutation(start, end, bank):
    from collections import deque
    bank_set = set(bank)
    if end not in bank_set:
        return -1
    mutations = {'A': 'TCG', 'C': 'TAG', 'G': 'TAC', 'T': 'AGC'}
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        gene, steps = queue.popleft()
        if gene == end:
            return steps
        for i, char in enumerate(gene):
            for new_char in mutations[char]:
                new_gene = gene[:i] + new_char + gene[i+1:]
                if new_gene in bank_set and new_gene not in visited:
                    visited.add(new_gene)
                    queue.append((new_gene, steps + 1))
    return -1