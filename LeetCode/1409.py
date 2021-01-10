class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        p = list(range(1,m+1)) # P=[1,2,3,4,...,m]
        print(p)
        ans = []

        for i in range(len(queries)):
            value = queries[i]
            position = p.index(value)
            ans.append(position)
            
            p.remove(value)
            p.insert(0, value)

        return ans