class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        summ = 0
        
        for i in range(len(nums)):
            if i==0 or nums[i-1] < nums[i]:
                summ += nums[i]
                
            else:
                summ = nums[i]
            res = max(res, summ)
        
        return res