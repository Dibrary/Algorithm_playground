n = 64
result = [n]
while n != 1:
    result.append(n//2)
    n = n//2

X = int(input())
if X in result:
    print(1)
else:
    cnt = 0
    while X != 0:
        for i in result:
            if i <= X:
                X = X - i
                cnt += 1
                break
    print(cnt)


## 다른 사람 코드 ##

X = int(input())
stick = [64]

while True:
    if sum(stick) <= X:
        break
    stick[-1] = stick[-1] // 2
    stick.append(stick[-1])
    if sum(stick[:-1]) >= X:
        del stick[-1]
print(len(stick))



n = int(input())
arr=[64]
while sum(arr)!=n:
    cnt = 0
    arr[0]/=2
    arr.append(arr[0])
    for i in range(len(arr)-1):
        cnt+=arr[i]
    if cnt>=n:
        arr.pop()
print(len(arr))


