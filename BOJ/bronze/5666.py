while True:
    try:
        h, p = map(int, input().split())
        print("{:.2f}".format(h/p))
    except:
        break

# 입력 갯수에 제한이 없을 때 위와 같이 try-except로 감싸야 됨.