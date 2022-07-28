n = int(input())
arr = list(map(int,input().split()))

tmp = [arr[0]+1]
for idx, i in enumerate(arr):
    if idx != 0:
        tmp.insert(len(tmp)-i,idx+1)

result = ""
for i in tmp:
    result += str(i) + " "
print(result[:-1])