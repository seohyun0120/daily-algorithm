class NumArray(object):
    def __init__(self, nums):
        self.sum = []
        
        count = 0
        for i in nums:
            count += i
            self.sum.append(count)

    def sumRange(self, i, j):
        if i > 0 and j > 0: 
            return self.sum[j] - self.sum[i-1]
        else:
            return self.sum[i or j]