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



def sample_generator():
    sample_key = ['A','B','C','D']
    source = ['molo','appl','adco']
    for s in sample_key:
        for o in source:
            yield [f'{s}_{o}']

for k in sample_generator():
    print(k)


# test sample code
# test
