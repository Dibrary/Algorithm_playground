
# 정렬 후에 앞 부분과 끝 부분을 교대로 계산해 나가면 될 듯

# n = int(input())
#
# tmp = list(map(int, input().split()))
# tmp.sort()
#
# start_idx = 0
# end_idx = len(tmp)-1
#
#
# result = 0
# slime = 0
#
# while start_idx < end_idx:
#     slime = tmp[start_idx] + tmp[end_idx]
#     result += tmp[start_idx] * tmp[end_idx]
#     start_idx += 1
#     end_idx -= 1
#
# if start_idx == end_idx:
#     result += slime * tmp[start_idx]
# print(start_idx, end_idx)

# 근데 위 처럼 하면 총합에서 이상함.
n = int(input())
tmp = list(map(int, input().split()))
tmp.sort()

start_idx = 0
end_idx = len(tmp)-1

result = 0
slime = 0

flag = 0 # 중간에 플래그를 넣어서 앞, 뒤 교대로 더하게 함.
while start_idx < end_idx:
    if start_idx == 0:
        slime = tmp[start_idx] + tmp[end_idx]
        result += tmp[start_idx] * tmp[end_idx]
        start_idx += 1
        end_idx -= 1
        flag = 1
    else:
        if flag == 1:
            result += slime * tmp[end_idx]
            slime = slime + tmp[end_idx]
            end_idx -= 1
            flag = 0
        elif flag == 0:
            result += slime * tmp[start_idx]
            slime = slime + tmp[start_idx]
            start_idx += 1
            flag = 1

if start_idx == end_idx:
    result += slime * tmp[start_idx]
print(result)