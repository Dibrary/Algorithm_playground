# n = int(input())
#
# for _ in range(n):
#     h, w, n = map(int, input().split())
#     row = 1+n//h
#     height = n%h
#
#     print(str(height)+"0"+str(row))

# 틀렸다고 함.

# n = int(input())
#
# for _ in range(n):
#     h, w, n = map(int, input().split())
#
#     if n%h == 0: row = int(n/h)
#     else:        row = int(1+n/h)
#
#     height = n%h
#     if height == 0:
#         height = h
#
#     print(str(height)+"0"+str(row))

# 이것도 틀림

n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split())

    if n%h == 0: row = int(n/h)
    else:        row = int(1+n/h)

    height = n%h
    if height == 0:
        height = h

    if len(str(row)) == 1:
        print(str(height)+"0"+str(row)) # 바로 이 부분이 틀렸었음. 2자리 수면 0이 들어가면 안 된다.
    else:
        print(str(height)+str(row))

