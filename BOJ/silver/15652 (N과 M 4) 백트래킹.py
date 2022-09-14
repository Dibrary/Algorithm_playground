

n, m = map(int, input().split())

def back_tracking(data, result, level):
    if level == m:
        tmp = sorted(result)
        if result == tmp:
            s = ""
            for i in result:
                s += str(i) + " "
            print(s[:-1])
            return
        else:
            return

    for i in range(len(data)):
        result.append(data[i])
        back_tracking(data, result, level + 1)
        result.pop()

data = [i for i in range(1, n + 1)]

back_tracking(data, [], 0)

# 위 코드 그냥 python으로는 시간초과 걸림
# pypy로는 통과




## 다른 사람 코드 ##

N,M = map(int,input().split())

def BT(index, letter):
        global ans
        if index > M-1:
            print(letter)
            return
        for i in range(1,N+1):
            if index == 0:
                BT(index+1, letter + str(i))
            else:
                if i >= int(letter[-1]):
                    BT(index+1, letter + " " + str(i))
BT(0,"")








def dfs(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n + 1):
        answer.append(i)
        dfs(i)
        answer.pop()


n, m = map(int, input().split())
# arr = [*range(0,n+1)]
answer = []
dfs(1)






from itertools import  combinations_with_replacement

N, M = map(int, input().split())
candidates = sorted(list(combinations_with_replacement(range(1, N + 1), M)))
for candidate in candidates:
    for member in candidate:
        print(member, end = " ")
    print("")










import sys

#def
def solve(start):
    if len(stack) == m:
        print(*stack)
        return
    for i in range(start, n+1):
        stack.append(i)
        solve(i)
        stack.pop()
#main
n, m = map(int, sys.stdin.readline().split())
stack = list()
solve(1)