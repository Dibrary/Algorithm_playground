
def solution(d, budget):
    d.sort()

    cnt = 0
    total = 0
    for i in d:
        if total + i <= budget:
            total += i
            cnt += 1
        else:
            break
    return cnt




## 다른 사람 코드 ##
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)









def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer







def solution(d, budget):
    s = 0
    j = 0
    d.sort()
    for i in range(len(d)):
        s += d[i]
        if s > budget:
            break
        else:
            j += 1
    return j