'''
입력한 숫자 값 만큼의 '수''박' 글자가 반복해서 나오게 하자.
'''

def solution(n):
    toggle = 0
    cnt = 0
    result = ''
    while cnt < n:
        if toggle%2 == 0:
            result += "수"
            cnt += 1
            toggle = 1
        elif toggle%2 == 1:
            result += "박"
            cnt += 1
            toggle = 0
    return result


## 다른 사람 코드 ##
def water_melon(n):
    s = "수박" * n
    return s[:n]






def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])






def water_melon(n):
    if n%2==0:
        return "수박"*int(n/2)
    else:
        return "수박"*int((n-1)/2) +"수"