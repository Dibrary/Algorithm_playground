
string = input().lower()

kangaroo_cnt = 0
kiwi_cnt = 0

for i in string:
    if i in "kangaro":
        kangaroo_cnt += "kangaroo".count(i) # count 갯수로 더해야 한다.
    if i in "kiwibird":
        kiwi_cnt += "kiwibird".count(i)

if kangaroo_cnt == kiwi_cnt:
    print("Feud continues")
elif kangaroo_cnt > kiwi_cnt:
    print("Kangaroos")
else:
    print("Kiwis")


