
def solution(n):
    table = [x for x in range(1,n+1)]

    cnt = 0
    for i in range(1, int(n//2)):
        for j in range(0, len(table)-i+1):
            if j == 0 and (sum(table[j:j+i]) > n):
                break
            if sum(table[j:j+i]) == n:
                cnt += 1
    return cnt

print(solution(15))

# 위 코드는 18개 중 3개 실패. 효율성 테스트는 단 하나도 통과 못함.
# 중간에 break부분 코드 제거 해도 3개는 실패.









