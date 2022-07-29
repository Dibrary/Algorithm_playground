
table = dict()
for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    table[s] = 0

n = int(input())

words = []
for _ in range(n):
    words.append(input()[::-1])

words.sort(key=lambda x: -len(x)) # 이렇게 해야 긴 순으로 나온다.

max_length = max([len(x) for x in words]) # 가장 긴 단어 값

temp = dict()
for i in range(max_length-1, -1, -1):
    for j in words:
        if len(j)-1 >= i:
            if i not in temp:
                temp[i] = set(j[i])
            else:
                temp[i].add(j[i])

no = 9

for k, v in zip(temp.keys(), temp.values()):
    for i in v:
        if table[i] == 0:
            table[i] = no
            no -= 1

result = 0
for i in words:
    sum_value = ""
    for m in i[::-1]:
        sum_value += str(table[m])
    result += int(sum_value)
print(result)

# 위 코드 런타임 에러 KeyError 나온다.
# dict에 key가 없는 것에 접근하려 할 때 발생.




table = dict()
for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    table[s] = 0

n = int(input())

words = []
for _ in range(n):
    words.append(input()[::-1])

words.sort(key=lambda x: -len(x))  # 이렇게 해야 긴 순으로 나온다.

max_length = max([len(x) for x in words])  # 가장 긴 단어 값

temp = dict()
for s in [x for x in range(11, -1, -1)]: # 미리 set을 넣어놓게 수정함.
    temp[s] = set()

for i in range(max_length - 1, -1, -1):
    for j in words:
        if len(j) - 1 >= i:
            temp[i].add(j[i])

no = 9

for k, v in zip(temp.keys(), temp.values()):
    for i in v:
        if table[i] == 0:
            table[i] = no
            no -= 1

result = 0
for i in words:
    sum_value = ""
    for m in i[::-1]:
        sum_value += str(table[m])
    result += int(sum_value)
print(result)

# 위 코드로 바꿔도 KeyError 난다.

'''
반례도 있었다.

10
ABB
BC
BC
BC
BC
BC
BC
BC
BC
BC

위 입력에 답은 1772인데, 1771로 나온다.
'''





## 다른 사람 코드 ##
# 이 코드에는 sys.stdin.readline 쓰면 틀려버린다.

n = int(input())
answer = 0
saving = {}
values = []
num = 9

for _ in range(n):
    word = input()
    for s in range(len(word)):
        if word[s] in saving:
            saving[word[s]] += 10 ** (len(word) - 1 - s)
        else:
            saving[word[s]] = 10 ** (len(word) - 1 - s)

for i in saving.values():
    values.append(i)

values.sort(reverse = True)

for j in values:
    answer += num * j
    num -= 1

print(answer)








import sys
m = sys.stdin.readline

# 입력 정보
w_num = int(m())
w_list = [list(map(str, m().strip())) for _ in range(w_num)]
w_info = {}

for i in range(w_num):
    for j in range(len(w_list[i])):
        if w_list[i][j] not in w_info:
            w_info[w_list[i][j]] = 10 ** (len(w_list[i]) - j - 1)

        else:
            w_info[w_list[i][j]] += 10 ** (len(w_list[i]) - j - 1)

new_info = sorted(w_info.items(), key=lambda x: x[1], reverse=True)

index = 9
answer = 0
for n in new_info:
    answer += n[1] * index
    index -= 1

print(answer)








import sys

n = int(sys.stdin.readline())

alpha = [] # 단어를 저장할 리스트
alpha_dict = {} # 단어 내의 알파벳별로 수를 저장할 딕셔너리
numList = [] # 수를 저장할 리스트

for i in range(n): # 단어를 입력받음
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n): # 모든 단어에 대해서
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 단어의 알파벳이 이미 dict에 있으면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) # 자리에 맞게 추가 ( 1의 자리면 1 )
        else:   # 자리에 없으면 새로 추가 ( 10의 자리면 10 )
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    numList.append(val)

numList.sort(reverse=True) # 수들을 내림차순 정렬

sum = 0
pows = 9
for i in numList: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1
print(sum)

