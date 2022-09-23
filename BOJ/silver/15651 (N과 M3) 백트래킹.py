
n, m = list(map(int ,input().split()))

def back_tracking(data, result, level):
    if level == m:
        s = ""
        for i in result:
            s += str(i ) +" "
        print(s[:-1])
        return

    for i in range(len(data)):
        result.append(data[i])
        back_tracking(data, result, level +1)
        result.pop()

data = [i for i in range(1, n+ 1)]

back_tracking(data, [], 0)


## 다른 사람 코드 ##
def f(i, k, r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            # if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
            #     used[j] = 1         # a[j] 사용됨으로 표시
            p[i] = a[j]         # p[i]는 a[j]로 결정
            f(i+1, k, r)         # p[i+1] 값을 결정하러 이동
                # used[j]= 0          # a[j]를 다른 자리에서 쓸 수 있도록 해제
N, R = map(int, input().split())

a= [i for i in range(1,N+1)]
# used = [0] * N
p = [0]*R
f(0,N, R)



## 책 풀이 ##
n, m = map(int, input().split())
answer = []

def backTracking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        backTracking(depth+1)
        answer.pop()

backTracking(0)


