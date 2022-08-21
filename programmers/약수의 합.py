

def solution(n):
    result = 0
    tmp = []
    for i in range(1, n//2+1):
        if n%i == 0 and i not in tmp and n//i not in tmp:
            tmp.append(i)
            tmp.append(n//i)
            result += (i + n//i)
    return result

# 위 코드는 17개 문제 중에 3개 틀림.




