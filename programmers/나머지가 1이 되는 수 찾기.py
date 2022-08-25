
def solution(n):
    for x in range(1, 10000000):
        if n % x == 1:
            return x


## 다른 사람 코드 ##

def solution(n):
    answer = 0

    for divisior in range(2, (n-1//2) +1) : #2부터~반값까지
        if (n-1) % divisior == 0: #약수가 있다면
            answer = divisior
            break #탈출
        else:
            answer = n-1 #약수가 없다면 본인
    return answer

