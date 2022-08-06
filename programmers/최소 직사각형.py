def solution(sizes):
    left = []
    right = []

    for a, b in sizes:
        if a > b:
            left.append(a)
            right.append(b)
        else:
            left.append(b)
            right.append(a)
    return max(left) * max(right)



## 다른 사람 코드 ##

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)






def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    return max([x[0] for x in sizes]) * max([x[1] for x in sizes])





import heapq as hq

def solution(sizes):
    widths, heights = [], []
    for s in sizes:
        hq.heappush(widths, -max(s)), hq.heappush(heights, -min(s))
    return hq.heappop(widths) * hq.heappop(heights)
