
'''
완전 탐색을 해야 한다는데, 완전탐색은 쉽다. 문제는, B, W를 칠할 때 WBWB이렇게 된 부분에서
갯수가 세어질지, 안세어질지 그걸 판단해야 한다.
만일 WWBWB이러면 갯수를 세면 안 되고, BWBWB 이러면 세도 되는건데...
'''

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))











## 책 풀이 ##

n, m = map(int, input().split())
board = []
answer = []

for _ in range(n):
    board.append(input())

for col in range(n-7):
    for row in range(m-7):
        countW = 0
        countB = 0
        for i in range(col, col+8):
            for j in range(row, row+8):
                if (i + j)%2 == 0:
                    if board[i][j] != 'W': countW += 1 # B로 되어있으면 W로 바꿔나갈 텐데, 이런 경우에는 -> 1
                    if board[i][j] != 'B': countB += 1 # W로 되어 있으면 B로 바꿔나갈텐데, 이런 경우에는 -> 2
                else:
                    if board[i][j] != 'B': countB += 1 # W로 바꾼 바로 옆에 바로 B로 바꿔야 한다. -> 1
                    if board[i][j] != 'W': countW += 1 # B로 바꾼 바로 옆에 바로 W로 바꿔야 한다. -> 2
        # 위 2중 for문에서 이미

        answer.append(countW)
        answer.append(countB)
print(min(answer))



