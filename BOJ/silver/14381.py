t = int(input())

for i in range(t):
    value = int(input())

    if value == 0:
        print("Case #%d: INSOMNIA"%(i+1))
    else:
        cnt = 1
        result = 0
        table = dict()
        while True:
            if len(table) == 10:
                break
            else:
                tmp = str(cnt*value)
                for s in tmp:
                    if s not in table:
                        table[s] = 1
                    else:
                        continue
                cnt += 1
        print("Case #%d: %d"%(i+1, int(tmp)))

# 예제는 통과하는데 제출 결과 실패.
# 아 CASE가 아니라 Case다. 통과!
