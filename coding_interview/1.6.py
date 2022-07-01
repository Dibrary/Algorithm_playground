s = "aabccccaaa"

result = ""
cnt = 1
for i in range(1, len(s)):

    if s[i-1] == s[i]:
        cnt += 1
    if s[i-1] != s[i]:

        result += str(s[i-1])+str(cnt)
        cnt = 1
result += str(s[-1])+str(cnt)
print(result)