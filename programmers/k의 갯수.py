
def solution(i, j, k):
    cnt = 0

    for x in range(i, j+1):
        table = str(x)
        for m in table:
            if m == str(k):
                cnt += 1
    return cnt

print(solution(1,13,1))
print(solution(10,50,5))


## 다른 사람 코드 ##

from collections import Counter

def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        answer += Counter(str(n))[str(k)]
    return answer







def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer