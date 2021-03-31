class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num = ''
        res = []
        
        for i in word:
            if '0'<=i<='9':
                num += i
                
            else:
                if len(num):                    
                    res.append(int(num))
                num = ''

        if len(num):
            res.append(int(num))

        return len(set(res))
