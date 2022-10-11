
import math
def solution(n): ## 순서쌍의 갯수
    cnt = 0
    result = []
    for k in range(1, int(math.sqrt(n))+1):
        if n%k == 0:
            result.append((n//k, k))
            cnt += 1
    if result[-1][0] == result[-1][1]:
        return (cnt-1)*2+1
    else:
        return cnt*2


## 다른 사람 코드 ##

def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            answer+=1
    return answer*2-1 if n**0.5==int(n**0.5) else answer*2







def solution(n):
    answer =0
    for i in range(n):
        if n % (i+1) ==0:
            answer +=1
    return answer