
start = 5

n = int(input())
if n == 1:
    print(start)
elif n == 2:
    print(start+7)
else:
    count = n-2
    start = 5+7

    for i in range(10, 30000004, 3):
        start += i
        count -=1
        if count == 0:
            break
    print(start%45678)

# 근데 일케 하면 시간이 꽤 걸린다.

### 다른 사람 풀이
n = int(input())
dot = 5
inc = 7
for i in range(1, n):
    dot += inc
    inc += 3
print(dot % 45678)



### 다른 사람 풀이
i=int(input())+1;print((i*(i+1)//2+i*(i-1))%45678)


