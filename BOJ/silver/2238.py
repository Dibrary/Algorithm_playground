
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

lower_value = values[0]

partition = partition_value[lower_value][0]
result = partition_name[partition][-1]

print(f"{partition} {result}")

# 9% 에서 틀림

