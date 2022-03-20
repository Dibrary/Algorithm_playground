import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_component = set(map(int, input().split()))
b_component = set(map(int, input().split()))

total = len(b_component-a_component) + len(a_component-b_component)
print(total)

