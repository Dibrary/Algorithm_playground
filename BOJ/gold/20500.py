length_arr = [0, 0, 1]
for i in range(3, 1516):
    if i % 2 == 0:
        length_arr.append(sum(length_arr[:i]) + 1)
    else:
        length_arr.append(sum(length_arr[:i]))

n = int(input())
result = length_arr[n] % 1000000007
print(result)



# result = []
# for i in range(0, 100000000):
#     result.append(str(i*15))
#     # print(str(i*15)[-3:]) # 여기서 규칙성을 찾을 수 있을듯.
#
# length_array = [0 for x in range(1, 12)] # 길이 갯수 만큼을 담아보았다.
#
# for i in result:
#     flag = 0
#     for s in "02346789":
#         if s in i:
#             flag = 1
#             break
#         else:
#             continue
#     if flag == 0:
#         length_array[len(i)] += 1
#         print(i)
# print(length_array)
#
# 위와 같이 코드 결과를 분석해서 아래의 결론을 얻음
# # 홀수번째는 앞에 모든 숫자들의 합
# # 짝수번째는 앞에 모든 숫자들의 합 +1