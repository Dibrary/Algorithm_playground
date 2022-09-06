
import sys
input = sys.stdin.readline

n = int(input())

solution = list(input().split()) # 정답
solution_table = dict()
for idx in range(len(solution)):
    if solution[idx] not in solution_table:
        solution_table[solution[idx]] = idx

submit = list(input().split()) # 제출값
submit_table = dict()
for idx in range(len(solution)):
    if submit[idx] not in submit_table:
        submit_table[submit[idx]] = idx

cnt = 0
for i in range(0, len(submit)-1):
    for j in range(i+1, len(solution)):
        if submit_table[solution[i]] < submit_table[solution[j]]:
            cnt += 1

under = int(len(solution)*(len(solution)-1)/2) # 분모
print(f"{cnt}/{under}")





## 다른 사람 코드 ##
n = int(input())
perfect_score = n * (n - 1) // 2

answer = input().split()
test = input().split()

answer_dic = {}
for idx, val in enumerate(answer):
    answer_dic[val] = idx

test_num = []
for i in test:
    test_num.append(answer_dic[i])

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if test_num[i] < test_num[j]:
            cnt += 1

print(f'{cnt}/{perfect_score}')











from itertools import combinations

n = int(input())

answer = list(map(str, input().split()))
hyun_woo = list(map(str, input().split()))
johab = list(combinations(hyun_woo, 2))

dic = dict()
i = 0
for j in answer:
    dic[j] = i
    i += 1

cnt = 0
for i in johab:
    x, y = i[0], i[1]
    if dic[x] < dic[y]:
        cnt += 1

dab = str(cnt) + "/" + str(n * (n - 1) // 2)
print(dab)
