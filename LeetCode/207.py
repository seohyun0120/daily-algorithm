class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        # 그래프 그리기
        for pair in prerequisites:
            a, b = pair
            graph[a].append(b)
        
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        
        return True
        
    
    def dfs(self, graph, visited, i):

        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True

        # 방문했다고 변경
        visited[i] = -1
        
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False

        # 모든 이웃 방문했으면 방문했다고 변경
        visited[i] = 1
        return True