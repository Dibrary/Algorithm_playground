def double_spot_remove(s):  # 중복되는 점 모두 제거
    tmp = ["." * x for x in range(2, len(s))]
    tmp.sort(reverse=True)  # 역순 해야 긴 것 부터 적용됨.

    for i in tmp:
        s = s.replace(i, ".")

    if len(s) == 1:
        if s == ".":
            return ""
        else:
            return s
    else:
        if s[0] == ".":
            s = s[1:]
        if s[-1] == ".":
            s = s[:-1]

    return s


def particle_char_remove(s):
    result = ""
    for i in s:
        if i.isalpha():
            result += i.lower()
        elif i.isdigit():
            result += i
        elif i in ["-", "_", "."]:
            result += i
    return result


def solution(new_id):
    answer = None

    new_id = particle_char_remove(new_id)
    new_id = double_spot_remove(new_id)

    if len(new_id) > 15:
        answer = new_id[:15]
    elif 2 < len(new_id) < 16:
        answer = new_id
    else:
        if len(new_id) < 3:
            if len(new_id) == 0:
                answer = "aaa"
            else:
                while len(new_id) < 3:
                    new_id = new_id + new_id[-1]
                answer = new_id
    answer = double_spot_remove(answer)
    return answer

# 내 코드 통과


### 다른 사람 코드 ###

import re # 정규표현식 사용.

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st



### 다른 사람 코드 ###

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

