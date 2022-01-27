n, m = map(int, input().split())

sites = dict()
for _ in range(n):
    site, pw = input().split()
    sites[site] = pw

result = []
for _ in range(m):
    want_to_find = input()
    if want_to_find in sites: # 이미 반드시 저장된 사이트 주소가 주어진다 했으니 이 조건문 필요 없음.
        result.append(sites[want_to_find])

for k in result:
    print(k)

# 틀림





