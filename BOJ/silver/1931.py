n = int(input())

times = []

for _ in range(n):
    times.append(list(map(int, input().split())))
times.sort(key=lambda x:x[1])

cnt = 0
end_time = 0
for i in range(len(times)):
    if i == 0:
        cnt += 1
        end_time = times[i][1]
    else:
        if times[i][0] >= end_time:
            cnt += 1
            end_time = times[i][1]
print(cnt)

# 88%에서 틀림.

