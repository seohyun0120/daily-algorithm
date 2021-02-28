class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        
        for n in intervals[1:]:
            # if overlapped?
            if n[0] <= res[-1][1]:
                # change interval's end
                res[-1][1] = max(n[1], res[-1][1])
            else:
                res.append(n)
        
        return res