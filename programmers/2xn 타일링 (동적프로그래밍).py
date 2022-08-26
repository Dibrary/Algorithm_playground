
# def solution(n):
#     arr = [0, 1, 2, 3, 5]
#
#     if n < 5:
#         return arr[n]
#     else:
#         for i in range(5, 60001):
#             arr.append(arr[i-1]+arr[i-2])
#         return arr[n]%1000000007

# 위 코드로 작성하면 테스트는 통과하나, 효율성(시간초과)로 다 실패함.

def solution(n):
    arr = [0, 1, 2, 3, 5]
    for i in range(5, 60001):
            arr.append((arr[i-1]+arr[i-2])%1000000007)

    return arr[n]
# 위 코드로 바꾸면 효율성 테스트를 통과할 뿐 아니라, 메모리도 적게 사용한다.




## 다른 사람 코드 ##

def tiling(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a%100000







def tiling(n):
    answer = 0
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    if len(str(b)) > 5:
        b = str(b)[-5:]
    answer = float(b)

    return answer