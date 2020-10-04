x = int(input())

for _ in range(x):
    n, m = map(int, input().split())
    
    result = 1
    if  n != m:
        for i in range(1, m+1):
            result *= i
        for i in range(1, m-n+1):
            result //= i
        for i in range(1, n+1):
            result //= i

    print(result)

# Combination
#mCn = m! / (m-n)!n!