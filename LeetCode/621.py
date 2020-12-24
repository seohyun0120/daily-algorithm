class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        task_list = sorted(dic.values(), reverse = True)
        
        i=0
        counter = 0
        while i<len(task_list) and task_list[i] == task_list[0]:
            counter += 1
            i+=1

        ret = (task_list[0] - 1) * (n+1) + counter
        
        return max(ret, len(tasks))