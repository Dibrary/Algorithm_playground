
from collections import deque

def solution(priorities, location):

    if len(priorities) == 1:
        print(1)
    else:
        tmp = [0 for _ in range(len(priorities))]
        tmp[location] = 1
        tmp = deque(tmp)

        values = deque(priorities)

        cnt = 0

        while values:
            if values[0] != max(values):
                values.append(values.popleft())
                tmp.append(tmp.popleft())
            else: # 최대값이 맞아
                cnt += 1
                if tmp[0] == 1: # 원하는 target이라면
                    return cnt
                else:
                    values.popleft()
                    tmp.popleft()
    return cnt



## 다른 사람 코드 ##

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # any라는게 있다.
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer











def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans









def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer