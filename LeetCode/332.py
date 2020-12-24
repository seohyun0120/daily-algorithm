class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        
        for start, end in tickets:
            if not graph.get(start, None):
                graph[start] = [end]
            else:
                # bisect.insort(graph[start], end)
                graph[start].append(end)
                graph[start].sort()
        
        visit = []
        def dfs(start):
            while graph.get(start, None):
                end = graph[start].pop(0)
                dfs(end)
            visit.append(start)
        
        dfs('JFK')
        return visit[::-1]