
def solution(n, stages):
    table = []

    total = len(stages)

    for i in range(n):
        table.append((i + 1, stages.count(i + 1) / total))
        total -= stages.count(i + 1)
        if total == 0:
            break

    table.sort(key=lambda x:(-x[1],x[0]))
    result = [k[0] for k in table]

    return result

# 위 코드는 예제 2개는 통과한다.
# 총 27문제 중 8개 실패 19개 통과.








