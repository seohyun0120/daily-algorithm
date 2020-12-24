x = int(input())

koong = [ 0 for i in range(68)]

koong[0] = 1
koong[1] = 1
koong[2] = 2
koong[3] = 4

for _ in range(x):
    N = int(input())

    for i in range(4, N+1):
        koong[i] = koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4]
    print(koong[N])