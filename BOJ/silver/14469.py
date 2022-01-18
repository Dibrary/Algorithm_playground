

n = int(input())
cows = []
for _ in range(n):
    cows.append(tuple(map(int, input().split())))

cows.sort(key=lambda x: x[0])

end_point = cows[0][0]+cows[0][1]

while True:
    for i in range(1, len(cows)):
        if cows[i][0] <= end_point:
            end_point += cows[i][1]
        elif cows[i][0] > end_point:
            end_point = cows[i][0]+cows[i][1]
    break
print(end_point)



