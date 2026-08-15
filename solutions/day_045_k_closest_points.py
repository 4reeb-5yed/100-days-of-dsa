import heapq

def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(heap, (dist, x, y))
    result = []
    for _ in range(k):
        dist, x, y = heapq.heappop(heap)
        result.append([x, y])
    return result