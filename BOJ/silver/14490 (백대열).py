'''
관건은 다 나눈 후에 언제 멈추느냐.
'''

import sys
input = sys.stdin.readline

string = list(map(int, input().split(":")))
if string[0] > string[1]:
    while True:
        cnt = 0
        for i in range(2, string[1]+1):
            cnt += 1
            if string[0]%i == 0 and string[1]%i == 0:
                string[0] = string[0]//i
                string[1] = string[1]//i
        if cnt == string[1]-1:
            break
else:
    while True:
        cnt = 0
        for i in range(2, string[0]+1):
            cnt += 1
            if string[0]%i == 0 and string[1]%i == 0:
                string[0] = string[0]//i
                string[1] = string[1]//i
        if cnt == string[0]-1:
            break

print(f"{string[0]}:{string[1]}")




## 다른 사람 코드 ##

import sys

def GCD(A, B):
	while B > 0:
		A, B = B, A%B
	return A

if __name__ == '__main__':
	a, b = map(int, sys.stdin.readline().rstrip().split(':'))
	now_gcd = GCD(a, b)
	print(f'{a//now_gcd}:{b//now_gcd}')












def GCD(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
            return GCD(a, b)
    return [str(a), str(b)]


s = input()
a = int(s[:s.index(':')])
b = int(s[s.index(':') + 1:])
l = GCD(a, b)
print(l[0] + ':' + l[1])