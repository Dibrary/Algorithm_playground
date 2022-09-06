
# def solution(n):
#     arr = [0, 0, 3, "모름", 11, ...] # 홀수 번째는 숫자가 올 수가 없다.

def solution(n):
    table = [0, 0, 3]
    for k in range(3, 5001):
        if k%2 != 0:
            table.append(0)
        else:
            table.append((table[k-2]*3 + sum(table[:k-2])*2 + 2)%1000000007)

    return table[n]

print(solution(4))


## 다른 사람 코드 ##

def solution(n):
    if n % 2:
        return 0
    front = back = 1
    for _ in range(n//2):
        front, back = back, (4*back - front) % 1000000007
    return back









def tiling(n):

    if n % 2 == 1:
        answer = 0
    elif n == 2:
        answer = 3
    elif n == 4:
        answer = 3*3 + 1*2
    else:
        result = [3, 3*3 + 1*2]
        for i in range(2, n//2):
            temp = result[i-1] * 3
            for k in range(0, i-1):
                temp += result[k] * 2
            result.append(temp + 2)
        answer = result[-1]%100000
    return answer











def tiling(n):
    if n % 2 == 1:
        return 0
    a = 1
    answer = 1
    sum = 0
    i = 2
    while i <= n:
        answer = a*3+sum*2
        sum += a
        a = answer
        i += 2
    return answer%100000