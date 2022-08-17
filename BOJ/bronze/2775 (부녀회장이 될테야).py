
def test(k, n):
    for i in range(0, k+1):
        for j in range(0, n):
            if i == 0: mem[i][j] = j+1
            elif j == 0: mem[i][j] = 1
            else:
                mem[i][j] = mem[i-1][j]+mem[i][j-1]
    return mem[k][n-1]


t = int(input())

for i in range(0, t):
    k = int(input())
    n = int(input())

    mem = [[0 for _ in range(0, n)] for i in range(0, k+1)]
    print(test(k, n))



## 다른 사람 코드 ##
tc = int(input())
for t in range(tc):
    k = int(input())  # 층
    n = int(input())  # 호수
    k_idx = [x for x in range(1, n + 1)]  # 0층 리스트 초기화 [1,2,3,4,...]

    for i in range(k):  # 층 수 만큼 반복
        for j in range(1, n):  # 1~n-1
            k_idx[j] += k_idx[j - 1]  # 층 별 각 호실 사람 변경
    print(k_idx[-1])  # 가장 마지막 수 출력








t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())

    f0 = [x for x in range(1, num + 1)]
    for k in range(floor):
        for i in range(1, num):
            f0[i] += f0[i - 1]
        # print(f0)
    print(f0[-1])