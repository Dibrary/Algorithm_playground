
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    n1 = 3*n
    n2 = 0
    if n1%2 == 0:  n2 = int(n1/2)
    else:          n2 = int((n1+1)/2)

    n3 = 3*n2
    n4 = int(n3/9)

    result = ""
    if n4%2 == 0: result = "odd"
    else:         result = "even"

    print("%d. "%(cnt) + result + " %d"%(n4))
    cnt += 1

# 왜 인지 실패. (예제와 결과는 같은데)
