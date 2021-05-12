class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []

        for q in queries:
            count = 0
            distance = q[2]**2
            
            for p in points:
                if (q[0]-p[0])**2 + (q[1]-p[1])** 2 <= distance:
                    count += 1
            
            ans.append(count)
        
        return ans