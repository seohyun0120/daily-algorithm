class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted(x for x,y in points)
        res = 0

        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]
            
            if res < diff:
                res = diff
        
        return res