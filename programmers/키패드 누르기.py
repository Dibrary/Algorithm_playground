
'''
관건은 중심에 있는 버튼을 '왼쪽 오른쪽'으로부터 얼마나 가까운지를 어떻게 측정하느냐.

'''

# left_length = {1:{2:1, 5:1.414, 8:2.236, 0:3.162},
#                4:{2:1.414, 5:1, 8:1.414, 0:2.236},
#                7:{2:2.236, 5:1.414, 8:1, 0:1.414},
#               "*":{2:3.162, 5:2.236, 8:1.414, 0:1}}
# right_length = {3:{2:1, 5:1.414, 8:2.236, 0:3.162},
#                6:{2:1.414, 5:1, 8:1.414, 0:2.236},
#                9:{2:2.236, 5:1.414, 8:1, 0:1.414},
#                "#":{2:3.162, 5:2.236, 8:1.414, 0:1}}
#
# left_last_position = "*"
# right_last_position = "#"
#
# result = ""
#
# for x in numbers:
#     if x in [1, 4, 7]:
#         result += "L"
#         left_last_position = x
#     elif x in [3, 6, 9]:
#         result += "R"
#         right_last_position = x
#     else:
#         print(left_last_position)
#         LL = left_length[left_last_position][x]
#         RL = right_length[right_last_position][x]
#         if LL > RL:
#             result += "R"
#             right_last_position = x
#         elif LL < RL:
#             result += "L"
#             left_last_position = x
#         elif LL == RL:
#             if hand == "right":
#                 result += "R"
#                 right_last_position = x
#             else:
#                 result += "L"
#                 left_last_position = x

# 여기까진 되었는데, 중앙부분에서 다시 중앙부분으로 가는 경우는 정해져있지 않다.

# def solution(numbers, hand):
#     left_length = {1:{2:1, 5:1.414, 8:2.236, 0:3.162},
#                    2:{2:0, 5:1, 8:2, 0:3},
#                    4:{2:1.414, 5:1, 8:1.414, 0:2.236},
#                    5:{2:1, 5:0, 8:1, 0:2},
#                    7:{2:2.236, 5:1.414, 8:1, 0:1.414},
#                    8:{2:2, 5:1, 8:0, 0:1},
#                    0:{2:3, 5:2, 8:1, 0:0},
#                   "*":{2:3.162, 5:2.236, 8:1.414, 0:1}}
#     right_length = {2:{2:0, 5:1, 8:2, 0:3},
#                     3:{2:1, 5:1.414, 8:2.236, 0:3.162},
#                     5:{2:1, 5:0, 8:1, 0:2},
#                     6:{2:1.414, 5:1, 8:1.414, 0:2.236},
#                     8:{2:2, 5:1, 8:0, 0:1},
#                     9:{2:2.236, 5:1.414, 8:1, 0:1.414},
#                     0:{2:3, 5:2, 8:1, 0:0},
#                     "#":{2:3.162, 5:2.236, 8:1.414, 0:1}}
#
#     left_last_position = "*"
#     right_last_position = "#"
#
#     result = ""
#
#     for x in numbers:
#         if x in [1, 4, 7]:
#             result += "L"
#             left_last_position = x
#         elif x in [3, 6, 9]:
#             result += "R"
#             right_last_position = x
#         else:
#             LL = left_length[left_last_position][x]
#             RL = right_length[right_last_position][x]
#             if LL > RL:
#                 result += "R"
#                 right_last_position = x
#             elif LL < RL:
#                 result += "L"
#                 left_last_position = x
#             elif LL == RL:
#                 if hand == "right":
#                     result += "R"
#                     right_last_position = x
#                 else:
#                     result += "L"
#                     left_last_position = x
#     return result
#
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

## 예제는 다 통과하는데, 20개 테스트 중 8개 실패로 나온다.

