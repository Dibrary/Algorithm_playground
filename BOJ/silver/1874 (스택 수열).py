
'''
문제 이해하는데 좀 걸림 =_=;

입력으로 주어진 수열을 스택으로 만들 수 있느냐 이 말이다.
스택에는 1, 2, 3, 4 이렇게 차례대로 값을 넣고 빼고 하면서 주어진 수열을 만들 수 있어야 함.
'''

from collections import deque
#
# n = int(input())
# arr = [0 for _ in range(n)]
# for i in range(n):
#     arr[i] = (int(input()))
#
# tmp = deque() # 오른쪽으로만 넣고 뺀다면 스택으로 쓸 수 있다.
#
# cnt = 0
# result = []
#
# for i in range(1, 100010):
#     tmp.append(i)
#     result.append("+")
#     while i == arr[cnt]:
#         tmp.pop()
#         result.append("-")
#         cnt += 1
#         i -= 1 # 이게 끝 부분에서 안 맞는다, 큰 숫자 i로부터 -1을 해 봐야 원하는 값이 되는 게 아니므로..

# 여기서 어떻게 해야 할 지 모르는 것은, 한 번 값을 뺀 이후에 다시 뺄 수 있다면 그건 어떻게 처리할 것인가.
# 그리고 NO인 경우는 어떤 조건으로 뺄 것인가.

'''
스택의 가장 위 수가 만들어야 하는 수열의 수 보다 크면 수열을 출력할 수 없다.
'''


### 책 풀이 ###
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# stack = deque()
# num = 1
# result = True
# operators = []
#
# for i in range(len(arr)):
#     su = arr[i]
#     if su >= num:
#         while su >= num:
#             num += 1
#             stack.append(num)
#             operators.append("+")
#         stack.pop()
#         operators.append("-")
#     else:
#         n = stack.pop()
#         if n > su:
#             print("NO")
#             result = False
#             break
#         else:
#             operators.append("-")
#
# for i in operators:
#     print(i)

# 책의 JAVA코드를 그대로 옮겼는데 안 된다. 왜..?


## 다른 사람 코드 ##
n = int(input())
s = []
op = []
count = 1
temp = True # 가능한지 불가능한지 확인하려는 flag 용

for i in range(n):
    num = int(input()) # 입력 값을 받는다. 입력을 받으면서 동시에 처리한다.
    while count <= num: # count가 num 보다 작으면
        s.append(count)
        op.append('+') # 추가
        count += 1 # count 증가
                   # count 이 숫자로 인해 s 스택에 몇 까지 넣었는지 알 수 있다.

    if s[-1] == num: # s 맨 마지막과 같으면
        s.pop() # 값을 꺼낸다.
        op.append('-')
    else:
        temp = False

if temp == False: # 한 번이라도 불가능하다면 NO
    print('NO')
else:
    for i in op:
        print(i)








import sys
input = sys.stdin.readline

n = int(input().strip())
mystack = []
now = 0
calc = []
end = False
seq = []

for i in range(0, n):
    seq.append(int(input().strip()))

for num in seq:
    if now < num:
        while(now < num):
            now += 1
            mystack.append(now)
            calc.append('+')
        mystack.pop()
        calc.append('-')
    elif mystack[-1] == num:
        mystack.pop()
        calc.append('-')
    else:
        print("NO")
        end = True
        break

if end != True:
    print(*calc, sep='\n')







n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
stack = []
s = []
c = []
t = 1
for i in range(2*n):
    if stack == []:
        stack.append(t)
        c.append("+")
        t += 1
    else:
        if stack[-1] == arr[0]:
            arr.pop(0)
            s.append(stack.pop())
            c.append("-")
        else:
            stack.append(t)
            c.append('+')
            t += 1

if len(s) != n:
    print('NO')
else:
    print("\n".join(c))