# 2진수를 정수로 바꾸는 간단한 방법 중요

a = input()
tmp1 = int('0b'+a, 2)
b = input()
tmp2 = int('0b'+b, 2)

print("%d"%(int(bin(tmp1*tmp2)[2:])))