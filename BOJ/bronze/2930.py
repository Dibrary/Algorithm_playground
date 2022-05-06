
def match(r, n):
    if (r == "S" and n == "R") or (r == "P" and n == "S") or (r == "R" and n == "P"):
        return 0
    elif r == n:
        return 1
    elif (r == "S" and n == "P") or (r == "P" and n == "R") or (r == "R" and n == "S"):
        return 2

R = int(input())
R_status = input()

N = int(input())
N_status = []
for _ in range(N):
    N_status.append(input()) # 이게 관건이다.

result = 0
if N == 1:
    for i in range(R):
        result += match(R_status[i], N_status[i])
    print(result)
    print(2*R)
elif N == 2:
    for k in range(N):
        for i in range(R):
            result += match(R_status[i], N_status[k][i])
    print(result)

    # 여기에 최대 점수 계산








