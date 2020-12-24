x = int(input())

for i in range(x):
    n = int(input())
    tree = list(map(int,input().split()))
    tree.sort()
    result = 0
    for j in range(2,n):
        c = tree[j] - tree[j - 2]
        result = max(c, result)
    print(result)