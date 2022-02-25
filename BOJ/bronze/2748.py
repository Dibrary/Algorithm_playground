
arr = [0,1]
for i in range(1, 101):
    arr.append(arr[i]+arr[i-1])

n = int(input())
print(arr[n])

