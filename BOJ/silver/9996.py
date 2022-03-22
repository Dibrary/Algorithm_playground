import sys
input = sys.stdin.readline

n = int(input())

pattern = list(input())[:-1]

for _ in range(n):
    pattern_idx = 0
    string = list(input())[:-1]

    for s in string:
        if s == pattern[pattern_idx]:
            pattern_idx += 1
        if pattern_idx < len(pattern) and pattern[pattern_idx] == "*":
            pattern_idx += 1
        if pattern_idx == len(pattern):
            break
    if pattern_idx == len(pattern):
        print("DA")
    else:
        print("NE")

# 틀림


