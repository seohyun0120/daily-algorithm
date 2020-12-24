x = int(input())
meeting = []

for i in range(x):
    start, end = map(int, input().split())
    meeting.append([start, end])

meeting = sorted(meeting, key=lambda a: a[0])
meeting = sorted(meeting, key=lambda a: a[1])

end_time = 0
count = 0

for i, j in meeting:
    if i >= end_time:
        count += 1
        end_time = j

print(count)