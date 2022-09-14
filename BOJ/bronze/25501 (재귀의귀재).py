
global cnt

def recursion(s, l, r):
    global cnt
    cnt += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
for _ in range(n):
    cnt = 0
    string = input()
    print(isPalindrome(string), cnt)




## 다른 사람 코드 ##

def recursion(s, l, r,cnt):
    if l >= r: return 1,cnt+1
    elif s[l] != s[r]: return 0,cnt+1
    else: return recursion(s, l+1, r-1,cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)

[print(*isPalindrome(input())) for i in range(int(input()))]











import sys
input = sys.stdin.readline

TC = int(input())
count = 0

def recursion(s, left, right):
    global count
    count += 1
    if left >= right: return 1
    elif s[left] != s[right]: return 0
    else: return recursion(s, left+1, right-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(TC):
    count = 0
    string = input().rstrip()
    print(isPalindrome(string), count)