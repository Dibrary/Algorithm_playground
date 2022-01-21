
arr = list(map(int, input().split()))

table = [100,100,200,200,300,300,400,400,500]

flag = 0
for idx, i in enumerate(arr):
    if i > table[idx]:
        flag = 1
        print("hacker")
        break
if flag != 1:
    if sum(arr) >= 100:
        print("draw")
    else:
        print("none")