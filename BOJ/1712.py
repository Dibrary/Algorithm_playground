'''
손익분기점 찾는 문제,
'''

A, B, C = list(map(int, input().split()))
print(-1 if B>C else int(A/(C-B)+1))

# 위 처럼 수식을 구한 후에 바로 계산하는게 아니라면 시간초과됨.
# 처음에는 for문을 이용해서 cnt값 구하려고 했었음..  기억해두자.