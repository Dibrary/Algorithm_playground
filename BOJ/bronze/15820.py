
s1, s2 = map(int, input().split())

s1_flag = 0
s2_flag = 0

for i in range(s1):
    a, b = map(int, input().split())
    if a == b:
        continue
    else:
        s1_flag = 1

for j in range(s2):
    a, b = map(int, input().split())
    if a == b:
        continue
    else:
        s2_flag = 1

if s1_flag == 0 and s2_flag == 0:
    print("Accepted")
elif s1_flag == 1:
    print("Wrong Answer")
elif s1_flag == 0 and s2_flag == 1:
    print("Why Wrong!!!")


## 다른 사람 코드.##

s1,s2 = map(int,input().split())
cnt = 0
for i in range(s1):
    a,b= map(int,input().split())
    if a!=b:
        print('Wrong Answer')
        exit()
for j in range(s2):
    a,b= map(int,input().split())
    if a!=b:
        print('Why Wrong!!!')
        exit()
print('Accepted')
