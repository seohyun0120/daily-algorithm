class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []

        for i in range(n):
            arr.append(start + 2*i)
            if i == 0:
                ans = arr[i]
            else:
                ans ^= arr[i]
        
        return ans