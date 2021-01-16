from collections import deque

n, m = map(int, input().split())

def topologicalSort():
    for _ in range(n):
        if not dq:
            return
        
        target = dq.popleft()
        res.append(target)

        for v in graph[target]:
            indegree[v] -= 1

            if not indegree[v]:
                dq.append(v)

res = []
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1

dq = deque()

for i in range(1, n+1):
    if not indegree[i]:
        dq.append(i)

topologicalSort()

print(*res)