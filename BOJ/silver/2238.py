
# U, N = map(int, input().split())
#
# partition_value = dict()
# partition_name = dict()
# values = set()
#
# for _ in range(N):
#     name, value = input().split()
#     value = int(value)
#
#     values.add(value)
#     if value not in partition_value:
#         partition_value[value] = [name]
#     else:
#         partition_value[value].append(name)
#
#     if name not in partition_name:
#         partition_name[name] = [value]
#     else:
#         partition_name[name].append(value)
#
# values = list(values)
# values.sort()
#
# lower_value = values[0] # 가장 낮은 가격
#
# partition = partition_value[lower_value][0] # 가장 낮은 가격을 먼저 말한 사람
# result = partition_name[partition][-1] # 그 사람이 제시한 최고 가격? 최고 가격이 아니다.
#
# print(f"{partition} {result}")

# 9% 에서 틀림

import sys
input = sys.stdin.readline

U, N = map(int, input().split())

partition_value = dict()
partition_name = dict()
values = set()

for _ in range(N):
    name, value = input().split()
    value = int(value)

    values.add(value)
    if value not in partition_value:
        partition_value[value] = [name]
    else:
        partition_value[value].append(name)

    if name not in partition_name:
        partition_name[name] = [value]
    else:
        partition_name[name].append(value)

values = list(values)
values.sort()

lower_value = values[0] # 가장 낮은 가격

partition = partition_value[lower_value][0] # 가장 낮은 가격을 먼저 말한 사람
tmp = sorted(partition_name[partition]) # 리스트에서 가장 높은 값 뽑기 위해 정렬
print(tmp)
result = tmp[-1]

print(f"{partition} {result}")

# 위 코드 틀림

