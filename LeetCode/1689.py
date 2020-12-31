class Solution:
    def minPartitions(self, n: str) -> int:
        a = []
        for i in n:
            a.append(i)
            
        a.sort()
        return a[-1]