
n = int(input())
string = input()

for i in "JAVA":
    string = string.replace(i, "")

if len(string)==0:
    print("nojava")
else:
    print(string)

# 33%에서 틀린다.
# 공백 처리가 문제인거 같은데..


n = int(input())
string = input()

result = ""
for i in string:
    if i == "J" or i == "A" or i == "V": # 하나라도 해당이 되면,
        continue
    else:
        result += i

if len(result) == 0:
    print("nojava")
else:
    print(result)

# 이것도 틀림.


N = int(input())
S = input()
res = ''
for c in S:
    if c not in "JAVA":
        res += c # 공백도 추가된다.
print(res if res else "nojava")
# 이건 된다?
