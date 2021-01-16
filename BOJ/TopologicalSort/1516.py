from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
cost = [0] * (n+1)
res = [0] * (n+1)
dq = deque()

for i in range(1, n+1):
    build_input = list(map(int, input().split()))
    for idx, v in enumerate(build_input):
        if idx == 0:
            cost[i] = v
        else:
            while v != -1:
                graph[v].append(i)
                indegree[i] += 1
                break

#시작점인 경우
for i in range(1, n+1):
    if not indegree[i]:
        res[i] = cost[i]
        dq.append(i)

def topologicalSort():
    for _ in range(1, n+1):
        target = dq.popleft()

        #target의 연결점을 찾아서 값을 더해준다
        for v in graph[target]:
            res[v] = max(res[v], res[target] + cost[v])

            indegree[v] -= 1
            if not indegree[v]:
                dq.append(v)

topologicalSort()

for i in range(1, n+1):
    print(res[i])