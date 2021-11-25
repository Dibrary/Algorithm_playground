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