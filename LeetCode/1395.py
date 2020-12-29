class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        larger, smaller = [0]*n, [0]*n
        
        for i, r in enumerate(rating[:-1]):
            for next in rating[i+1:]:
                if next > r:
                    larger[i] += 1
                else:
                    smaller[i] += 1

        ans = 0
        for i, r in enumerate(rating[:-2]):
            for j, next in enumerate(rating[i+1:], start=i+1):
                
                if next > r:
                    ans += larger[j]
                else:
                    ans += smaller[j]

        return ans