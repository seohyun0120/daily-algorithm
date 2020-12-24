class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        
        for i, v in enumerate(T):
            while stack and v > T[stack[-1]]:
                last = stack.pop()
                ans[last] = i - last
            stack.append(i)
        return ans
