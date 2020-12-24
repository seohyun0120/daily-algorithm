case = int(input())

def fiboDP(i):
    if i == 0:
        print(1, 0)
    elif i == 1:
        print(0, 1)
    elif i == 2:
        print (1, 1)
    else:
        temp = 0
        cur = 1
        before = 0
        for _ in range(i-1):
            temp = cur
            cur = before + temp
            before = temp
        
        print(before, cur)

for _ in range(case):
    num = int(input())
    fiboDP(num)