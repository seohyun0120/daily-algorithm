class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        self.dfs(nums, [], ans)
        
        return ans
        
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)