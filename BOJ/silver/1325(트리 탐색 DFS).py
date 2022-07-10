
'''
트리 자료구조를 만들고,
해당 번호별로 한 번에 많이 한다는 것은, DFS로 끝까지 들어가는 갯수를 센 뒤에
그 갯수에 대한 노드를 오름차순으로 하면 될까?
'''


n, m = map(int ,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

# [[], [3], [3], [1, 2, 4, 5], [3], [3]] 예제 입력은 이렇게 구성되는데,
# 왜 결과가 1, 2 가 나오는지 모르겠다.




