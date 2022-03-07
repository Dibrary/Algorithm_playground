
arr = [1]
start = 2
for i in range(1, 1001):
    arr.append(arr[-1]+start*i)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(f'{n} => {arr[n-1]}')



