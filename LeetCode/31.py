class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n < 2:
            return nums
        
        peak = -1
        i = n-2
        
        while i >= 0:
            if nums[i] < nums[i+1]:
                peak = i
                break
            i -= 1
        
        print(peak)
        if peak < 0:
            nums.sort()
            return nums
        
        idx = n-1
        
        while idx >= 0:
            if nums[peak] < nums[idx]:
                nums[peak], nums[idx] = nums[idx], nums[peak]
                break
            idx -= 1
            
        nums[peak+1:] = reversed(nums[peak+1:])
        return nums