import sys

a = int(input())
lst = []

for _ in range(a):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        lst.append(int(cmd[1]))

    elif cmd[0] == "pop":
        if len(lst) > 0:
            print(lst[-1])
            lst.pop()
        else:
            print(-1)

    elif cmd[0] == "size":
        print(len(lst))

    elif cmd[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "top":
        if len(lst) > 0:
            print(lst[-1])
        else:
            print(-1)