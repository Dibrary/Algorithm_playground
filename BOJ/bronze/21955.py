
import sys
input = sys.stdin.readline

n = input()
mid_idx = len(n)//2
print(f'{n[:mid_idx]} {n[mid_idx:]}')



