
def solution(n):
    arr = [0,1,1]
    for k in range(3, 100001):
        arr.append((arr[k-1]+arr[k-2])%1234567) # 미리 나머지로 넣어놔야 실행시간 및 메모리를 줄일 수 있다.
    return arr[n]


## 다른 사람 코드 ##

def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a







def fibonacci(num):
    answer = [0,1]

    for i in range(2,num+1):
        answer.append(answer[i-1]+answer[i-2])
    #print(answer)

    return answer[-1]