
# 정렬 후에 앞 부분과 끝 부분을 교대로 계산해 나가면 될 듯

n = int(input())

tmp = list(map(int, input().split()))

start_idx = 0
end_idx = len(tmp)-1


result = 0
slime = 0

while start_idx < end_idx:
    slime = tmp[start_idx] + tmp[end_idx]
    result += tmp[start_idx] * tmp[end_idx]
    start_idx += 1
    end_idx -= 1

if start_idx == end_idx:
    result += slime * tmp[start_idx]
print(start_idx, end_idx)

