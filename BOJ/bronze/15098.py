import sys
input = sys.stdin.readline

s = input().split()
flag = 0
for i in s:
    if s.count(i) != 1:
        print("no")
        flag = 1
        break
if flag == 0:
    print("yes")


