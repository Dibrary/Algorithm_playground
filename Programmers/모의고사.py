
def calculate(answer, student):
    cnt = 0
    for i in range(0, len(answer),len(student)):
        tmp = answer[i:i+len(student)]
        for idx, i in enumerate(tmp):
            if student[idx] == i:
                cnt += 1
    return cnt


def solution(answer):

    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    collect_values = []
    collect_values.append(calculate(answer,first))
    collect_values.append(calculate(answer,second))
    collect_values.append(calculate(answer,third))

    answer = []
    max_value = max(collect_values)
    for idx, i in enumerate(collect_values):
        if i == max_value:
            answer.append((idx+1))

    answer.sort()
    return answer

# 내 풀이 통과.


# 다른 사람 풀이

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# 다른 사람 풀이
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
