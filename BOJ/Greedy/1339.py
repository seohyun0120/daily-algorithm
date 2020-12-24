x = int(input())

word = []
number = [9,8,7,6,5,4,3,2,1]
for i in range(x):
    word.append(list(input().strip()))

alphabet = [0 for i in range(26)]

for i in word:
    for j in range(len(i)):
        alphabet[ord(i[j]) - 65] += 10 ** (len(i) - j -1)

alphabet.sort(reverse=True)

result, count = 0, 9

for i in alphabet:
    result += count * i
    count -= 1

print(result)