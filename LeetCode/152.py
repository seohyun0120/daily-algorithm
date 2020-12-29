class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mn = ans = nums[0]
        
        for i in range(1, len(nums)):
            cur = nums[i]
            a = mx * cur
            b = mn * cur

            mx = max(cur, max(a,b))
            mn = min(cur, min(a,b))
            
            ans = max(ans, mx)
        
        return ans