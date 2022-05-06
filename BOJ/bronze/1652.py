
# n = int(input())
#
# room_position = [] # 초기 자리 정보 저장
# for _ in range(n):
#     room_position.append(list(input()))
#
# horizontal_cnt = 0
# vertical_cnt = 0
#
# for i in range(len(room_position)):
#     for j in range(len(room_position[0])-1):
#         if room_position[i][j] == '.' and room_position[i][j+1] == '.':
#             horizontal_cnt += 1
#             break # 여기서 바로 break를 해 버리면 안 된다.
#
# for i in range(len(room_position)-1):
#     for j in range(len(room_position[0])):
#         if room_position[i][j] == '.' and room_position[i+1][j] == '.':
#             vertical_cnt += 1
#             break
#
# print(f'{horizontal_cnt} {vertical_cnt}')

# 위 코드 틀림

'''
..X..
X..X.
..X..
.X..X
..X..

이렇게 했을 때 가로는 8, 세로는 4가 나와야 한다.
위 코드로는 가로 5, 세로 4가 나온다.
'''

n = int(input())

room_position = [] # 초기 자리 정보 저장
for _ in range(n):
    room_position.append(list(input()))

horizontal_cnt = 0
vertical_cnt = 0

for i in range(len(room_position)):
    for j in range(len(room_position[0])-1):
        if room_position[i][j] == '.' and room_position[i][j+1] == '.':
            horizontal_cnt += 1
            break

for i in range(len(room_position)-1):
    for j in range(len(room_position[0])):
        if room_position[i][j] == '.' and room_position[i+1][j] == '.':
            vertical_cnt += 1
            break

print(f'{horizontal_cnt} {vertical_cnt}')
