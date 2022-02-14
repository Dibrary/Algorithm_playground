t = int(input())
numbers = list(map(int, input().split()))[::-1]

P, Q = 0,0

for i in range(0, len(numbers)-1):
    if i == 0:
        P = numbers[i]*numbers[i+1]+1
        Q = numbers[i]
    else:
        P = Q*numbers[i+1]+P
    P, Q = Q, P
print("%d %d"%(Q-P, Q))