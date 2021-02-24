class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(start, result):
            if len(result) == k:
                res.append(list(result))
                return
            
            for i in range(start, n+1):
                if k - len(result) - 1 > (n-i):
                    break
                result.append(i)
                dfs(i+1, result)
                result.pop()
        
        dfs(1, [])
        return res