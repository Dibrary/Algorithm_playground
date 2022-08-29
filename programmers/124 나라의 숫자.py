
# 3진법으로 바꾼 후에 3진법 값 마다 1,2,4를 배치하는 방법이 먼저 떠오름.


cnt = 1
for n in range(1, 11):
    result = ""
    while n > 2:
        result += str(n%3)
        n = n//3
    result += str(n)
    print(cnt, result[::-1])
    cnt += 1

# 약간 여기서 뭔가 힌트를 얻을 수 있을 거 같은데.
# 10을 4로 바꾸면 되긴 하는데, 규칙성이 없는 부분이 하나 있다.




