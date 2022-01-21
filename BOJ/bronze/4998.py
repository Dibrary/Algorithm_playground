
n, b, m = map(float, input().split())

cnt = 0
for i in range(300000):
    n *= 1+(b/100)
    cnt += 1
    if n >= m:
        break
print(n, cnt)

'''
소수점 2째자리까지 가능하다고 해서
0.01 0.01 1000000으로 하면 약 4만번 좀 안되는 곳에서 멈춘다. 
'''