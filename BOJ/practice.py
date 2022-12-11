#
# n = int(input())
#
# ball = 1
#
# for i in range(n):
#     x, y = map(int, input().split())
#     if x == ball or y == ball:
#         if x == ball:
#             ball = y
#         elif y == ball:
#             ball = x
# print(ball)


W = []
K = []
for i in range(20):
    if i < 10:
        W.append(int(input()))
    else:
        K.append(int(input()))
W.sort(); K.sort()
print("%d %d"%(sum(W[-3:]),sum(K[-3:])))



# this is sample code
# this is sample code 2

def gener():
    for x in range(10):
        for y in range(10):
            yield x+y

for k in gener():
    print(k)





