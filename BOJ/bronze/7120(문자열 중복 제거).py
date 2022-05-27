
s = input()

table = set()
result = ""
for i in s:
    if i not in table:
        result += i
        table.add(i)

print(result)
# 틀렸대
# 아 위 코드는 반례가 있다. ooooooonnniiiiooooooonnnn 하면 안됨.


s = input()
s = s+"O" # 맨 끝에 값까지 처리하고자 임의의 문자 추가 (대문자는 안쓴다고 했으니 대문자를 넣음)
result = ""
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue
    else:
        result += s[i]
print(result)