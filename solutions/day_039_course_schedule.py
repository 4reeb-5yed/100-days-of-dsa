def can_finish(num_courses, prerequisites):
    from collections import deque
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    completed = 0
    
    while queue:
        course = queue.popleft()
        completed += 1
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    return completed == num_courses