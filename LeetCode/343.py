class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        
        ans = 1
        # k should be either 2 or 3
        # k should be 3 as much as possible (3*3 > 2*2*2)
        
        while n>4:
            ans*=3
            n-=3
        
        ans*=n
        return ans