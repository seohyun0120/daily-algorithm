class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        result = []
        
        if size < 3:
            return []
        
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            c = nums[i]*-1
            start, end = i+1, size-1

            while start < end:
                if nums[start] + nums[end] == c:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif nums[start] + nums[end] < c:
                    start += 1
                else:
                    end -= 1
        return result