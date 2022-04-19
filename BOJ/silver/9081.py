
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = []
    string = input()
    for i in permutations(list(string), len(string)):
        if i not in arr:
            arr.append(i)
    arr.sort()
    if arr.index(tuple(string)) == len(arr)-1:
        print(string)
    else:
        print("".join(map(str,arr[arr.index(tuple(string))+1])))

# 위 코드 시간초과 걸림






