import sys
input = sys.stdin.readline


t = int(input())
first = input()
second = input()

cnt = 0
for i in range(0, len(first)):
    if first[i] != second[i]:
        cnt += 1
print(cnt)