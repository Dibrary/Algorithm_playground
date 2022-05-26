#
# x = [[] for _ in range(10)]
#
# for i in range(1,11):
#     x[0].append(i)
# for k in range(0, 10):
#     x[1].append(sum(x[0][:k+1]))
# for j in range(0, 10):
#     x[2].append(sum(x[1][:j+1]))
# for j in range(0, 10):
#     x[3].append(sum(x[2][:j+1]))
# for j in range(0, 10):
#     x[4].append(sum(x[3][:j+1]))

    # 이런식으로 구하면 해당 위치의 값을 알 수 있으나, for문에 for문이 도는 꼴이라 n**2의 복잡도 걸림







