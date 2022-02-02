
string = input()

for i in ["a","e","i","o","u"]:
    string = string.replace("p"+i,"")
print(string)

# 이거 틀림. 아무래도 글자 지운 후에 다시 p"ㅌ"꼴 글자가 있으면 그것이 남는듯.


