x = int(input())

fibo = [1,2]
for i in range(2,46):
    fibo.append(fibo[i-1] + fibo[i-2])

for i in range(x):
    n = int(input())
    result = []
    while(n):
        for k in range(46):
            if(fibo[k] <= n):
                t = fibo[k]
        n -= t
        result.append(t)
        result.sort()
    print(*result)