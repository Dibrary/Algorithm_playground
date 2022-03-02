
try:
    arr = []
    while True:
        arr.append(int(input()))
except:
    tmp = [x for x in range(1, max(arr)+1)]
    flag = 0
    for i in tmp:
        if i not in arr:
            print(i)
            flag = 1
    if flag == 0:
        print("good job")

