
'''
문제가 잘 이해가 안 된다.
딱 2개 말고 여러 개가 가능하다는 사례는 뭘까?

'''

def adding(table, value):
    if value not in table:
        table[value] = 1
    else:
        table[value]+= 1

n = int(input())

groups = []

start = dict()
end = dict()

for _ in range(n):
    s, e = map(int, input().split())
    groups.append([s,e])
    adding(start, s)
    adding(end, e)

q = int(input())
check = []
for _ in range(q):
    s, e = map(int, input().split())
    cnt = 0
    if s in start and e in end:
        cnt += (start[s] + end[e])
        print(cnt)
    else:
        print(-1)

# 그냥 위 처럼 해버리면 2 6, 4 8 에서 있는 것으로 취급해버린다. (예상 출력 -1, 실제 출력 2가 됨)






