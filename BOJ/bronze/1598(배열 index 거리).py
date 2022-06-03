
# 우선 4개 숫자 단위로 끊는 방법은 아래와 같다.
# value = []
# tmp = []
# for i in range(1,20):
#     if i%4 == 0:
#         tmp.append(i)
#         value.append(tmp)
#         tmp = []
#     else:
#         tmp.append(i)
# print(value)
'''
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

'''
######################################



a, b = map(int, input().split())

wide_length = ((b-a)//4)+1 # 이렇게 하면 수평 거리는 나온다.
vertical_length = abs(a%4 - b%4) # 수직 거리가 문제다.
print(wide_length+vertical_length)

# 예제만 맞지 11, 39로 하면 안 맞는다.
