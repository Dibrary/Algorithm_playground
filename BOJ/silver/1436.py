import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

for i in range(3000000):
    if '666' in str(i):
        cnt += 1
        if cnt == n:
            print(i)
            break

## 다른 사람 코드 ##

N = int(input())

def check(n):
    nums = []
    while n != 0:
        nums.append(n % 10)
        n //= 10

    for i in range(len(nums)-2):
        if nums[i] == 6 and nums[i+1] == 6 and nums[i+2] == 6:
            return True

    return False

cnt = 0
i = 0
while cnt != N:
    i += 1
    if check(i):
        cnt += 1
print(i)








n = int(input())

number = 666

while True:
    if "666" in str(number):
        n -= 1
    if n == 0:
        break
    number += 1
print(number)