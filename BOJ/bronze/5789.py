import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input()
    b = len(string) // 2
    a = b+1

    if string[a] == string[b]:
        print("Do-it")
    else:
        print("Do-it-Not")



