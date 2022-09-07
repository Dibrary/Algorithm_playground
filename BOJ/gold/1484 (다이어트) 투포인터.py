
g = int(input())

start_idx = 1
end_idx = 2

result = []

while start_idx < end_idx:
    if (end_idx*end_idx - start_idx*start_idx) == g:
        result.append(end_idx)
        end_idx += 1
    elif (end_idx*end_idx - start_idx*start_idx) > g:
        start_idx += 1
    elif (end_idx*end_idx - start_idx*start_idx) < g:
        end_idx += 1

if result == []:
    print(-1)
else:
    result.sort()
    print("\n".join(map(str, result))) # 결과 출력할 때 여러 개면 이렇게 하는게 편함.


## 다른 사람 코드 ##


g = int(input())
a = [i*i for i in range(1,100000)]

l = 0
flag = 1
for r in range (len(a)):
  if a[r] - a[l] >= g :
    while a[r] - a[l] >= g :
      if a[r] - a[l] == g :
        print(int(a[r]**0.5))
        flag = 0
      l += 1
if flag:
  print(-1)









g = int(input().strip())
weight = list()

left, right = 1, 2
while left < g:
    diff = (right + left)*(right - left)
    if diff == g:
        weight.append(right)
        left += 1
    elif diff > g:
        left += 1
    elif diff < g:
        if right < g:
            right += 1
        else:
            left += 1
if weight:
    print('\n'.join(map(str, weight)))
else:
    print(-1)










G = int(input()) # G는 100,000보다 작거나 같은 자연수이다.

arr = [i for i in range(0, 50001)]

past = 1
now = 1
answer = []
while past < 50001 and now < 50001:
    g = (arr[now] + arr[past]) * (arr[now] - arr[past])

    if g == G:
        answer.append(now)
    if g < G:
        now += 1
        continue
    past += 1

if not answer:
    print(-1)
else:
    for a in answer:
        print(a)