class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_seen = {}
        max_index, count = 0, 0
        result = []
        
        for i, char in enumerate(S):
            last_seen[char] = i
        
        for i, char in enumerate(S):
            max_index = max(max_index, last_seen[char])
            count+= 1
            
            if i == max_index:
                result.append(count)
                count = 0
            
        return result