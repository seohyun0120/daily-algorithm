## 시간 초과 해결 방법: print() -> sys.stdin.readline()으로 변경
import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    dq = deque()
    ans = [0] * (n+1)

    for _ in range(1, k+1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    
    w = int(sys.stdin.readline())
    for i in range(1, n+1):
        if not indegree[i]:
            ans[i] = time[i-1]
            dq.append(i)

    for _ in range(1, n+1):
        target = dq.popleft()

        for v in graph[target]:
            ans[v] = max(ans[v], ans[target] + time[v-1])

            indegree[v] -= 1
            if not indegree[v]:
                dq.append(v)

    print(ans[w])