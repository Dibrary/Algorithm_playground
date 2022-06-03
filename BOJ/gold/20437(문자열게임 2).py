
t = int(input())

for _ in range(t):
    w = input()
    words= set(w) # 이렇게 하면 각 문자들 별로 최소 1번은 확인 가능

     # 어떤 문자를 K개 포함하는지 확인하는 방법에 for문 2겹을 하면 n**2 시간이 걸림;;


