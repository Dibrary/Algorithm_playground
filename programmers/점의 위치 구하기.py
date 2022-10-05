
def solution(dot):
    first, second = dot
    if first < 0 and second > 0:
        return 2
    elif first < 0 and second < 0:
        return 3
    elif first > 0 and second > 0:
        return 1
    else:
        return 4


## 다른 사람 코드 ##

def solution(dot):
    a, b = 1, 0
    if dot[0]*dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2*a-b






def solution(dot):
    x,y = dot
    if x*y>0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2








