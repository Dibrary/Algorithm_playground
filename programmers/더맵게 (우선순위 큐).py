# import heapq
#
# def solution(scoville, K):
#     q = []
#     for x in scoville:
#         heapq.heappush(q, x)
#     cnt = 0
#     while q:
#         first = heapq.heappop(q)
#
#         if first < K:
#             second = heapq.heappop(q)
#             heapq.heappush(q, first + (second * 2))
#             cnt += 1
#         else:
#             break
#     return cnt

# 위 코드 효율성테스트 모조리 통과 하는데, 런타임 에러가 4개 나온다.
# "모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다." 이 조건이 있다. 실행해 보니 index out of range 라는 에러가 난다.


import heapq

def solution(scoville, K):
    q = []
    for x in scoville:
        heapq.heappush(q, x)
    cnt = 0
    flag = 0

    while q:
        first = heapq.heappop(q)

        if first < K:
            if len(q) == 0:
                flag = 1 # 이 경우에는 아예 꺼낸 값이 K보다 작은데 그거 하나 뿐이라는 얘기.
                break
            second = heapq.heappop(q)
            heapq.heappush(q, first + (second * 2))
            cnt += 1
        else:
            heapq.heappush(q, first)
            break
    if flag == 1:
        return -1
    else:
        return cnt




## 다른 사람 코드 ##
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer










import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    size, cnt = len(scoville) - 1, 0
    f = heapq.heappop(scoville)
    while size > 0:
        s = heapq.heappop(scoville)
        f = heapq.heappushpop(scoville, f + s + s)
        if f >= K:
            return cnt + 1
        cnt += 1
        size -= 1
    return -1