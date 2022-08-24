
from collections import deque
key = {')':'('}

string = input()

result = 0
stack = deque()

for idx, k in enumerate(string):
    flag = 0
    if k not in key:
        stack.append(k)
        flag = 0
    else:
        if k == ')' and string[idx-1] != '(':
            flag += 1 # 이걸 왜 넣었냐면, 중간에 잘리는 막대인 경우, 모두 갯수 세면 다음에 자를 때 몇 개를 빼야 할 지 모름.
            result += flag # 그래서 해당 위치에서 끝나는 막대 갯수만 세고 다음번에 자를 때 나머지 막대를 같이 세개 함.
            stack.pop()
        else:
            stack.pop()
            result += len(stack)
            flag = 0
print(result)



## 다른 사람 코드 ##


string = input()
string = "-".join(string.split("()"))
stack = []
result = 0
cnt = 0
for s in string:
    if s == "(":
        stack.append(s)
        cnt += 1
    elif s == "-":
        result += cnt
    elif s == ")":
        stack.pop()
        result += 1
        cnt -= 1
print(result)











gualho = input()
makde = 0
ans = 0
for i in range(len(gualho)-1):

    # ()가 아닌 (가 있는 경우는 막대의 시작 부분
    if gualho[i] == '(' and gualho[i+1] != ')':
        ans += 1 # 기본 막대 개수가 추가됨
        makde += 1 # 막대가 하나 쌓임

    # ()가 아닌 )가 있는 경우는 막대의 끝 부분
    elif gualho[i] == ')' and gualho[i-1] != '(':
        makde -= 1 # 막대가 하나 빠짐

    # ()인 경우는 레이저
    elif gualho[i] == '(' and gualho[i+1] == ')':
        ans += makde # 쌓여있는 막대들을 잘라 막대 개수가 추가됨

print(ans)











input_string = input()

stack = 0
laser = 0
output = 0

for i in input_string:
    if i == '(':
        if laser == 0:
            laser = 1
        elif laser == 1:
            stack += 1
    elif i == ')':
        if laser == 1:
            laser = 0
            output += stack
        elif laser == 0:
            output += 1
            stack -= 1

print(output)

