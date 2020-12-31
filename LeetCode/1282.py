class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupDic = {}        
        for idx,value in enumerate(groupSizes):
            if value in groupDic:
                groupDic[value].append(idx)
            else:
                groupDic[value] = [idx]
        
        ans = []
        
        for i in groupDic:
            for j in range(0, len(groupDic[i]), i):
                ans.append(groupDic[i][j:j+i])

        return ans