# import copy
#
# values = list(map(int, input().split()))
# values2 = copy.deepcopy(values)
#
# max_value = values.index(max(values)) ;    values[max_value] = 0
# second_value = values.index(max(values)) ; values[second_value] = 0
# third_value = values.index(max(values)) ;  values[third_value] = 0
#
# if max_value == 0 and second_value == 1 and third_value == 2:
#     print((values2[max_value] * values2[second_value]) // values2[third_value])
#
# elif max_value == 0 and second_value == 2 and third_value == 1:
#     print((values2[max_value] // values2[third_value]) * values2[second_value])
#
# elif max_value == 1 and second_value == 0 and third_value == 2:
#     print((values2[max_value] * values2[second_value]) // values2[third_value])
#
# elif max_value == 1 and second_value == 2 and third_value == 0:
#     print((values2[max_value] // values2[third_value]) * values2[second_value])
#
# elif max_value == 2 and second_value == 0 and third_value == 1:
#     print((values2[second_value] // values2[third_value]) * values2[max_value])
#
# elif max_value == 2 and second_value == 1 and third_value == 0:
#     print((values2[second_value] * values2[third_value]) // values2[max_value])

# 위 코드 2% 에서 곧바로 틀림.

# import copy
#
# values = list(map(int, input().split()))
# values2 = copy.deepcopy(values)
#
# max_value = values.index(max(values)) ;    values[max_value] = 0
# second_value = values.index(max(values)) ; values[second_value] = 0
# third_value = values.index(max(values)) ;  values[third_value] = 0
#
# if max_value == 0 and second_value == 1 and third_value == 2:
#     print(int((values2[max_value] * values2[second_value]) / values2[third_value]))
#
# elif max_value == 0 and second_value == 2 and third_value == 1:
#     print(int((values2[max_value] / values2[third_value]) * values2[second_value]))
#
# elif max_value == 1 and second_value == 0 and third_value == 2:
#     print(int((values2[max_value] * values2[second_value]) / values2[third_value]))
#
# elif max_value == 1 and second_value == 2 and third_value == 0:
#     print(int((values2[max_value] / values2[third_value]) * values2[second_value]))
#
# elif max_value == 2 and second_value == 0 and third_value == 1:
#     print(int((values2[second_value] / values2[third_value]) * values2[max_value]))
#
# elif max_value == 2 and second_value == 1 and third_value == 0:
#     print(int((values2[second_value] * values2[third_value]) / values2[max_value]))
# //를 / 하나로 바꾸고 int 씌우니까 32%까지는 진행됨.


# 관점을 바꿔야 한다. a, b, c 각 경우에 대해 모든 걸 할 게 아니라.
# 연산자 2개를 넣을 수 있는 경우가 2개 뿐이다.

a, b, c = map(int, input().split())
print(int(max((a*b)/c, (a/b)*c)))

