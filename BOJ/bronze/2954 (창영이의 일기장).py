
# string = input()
#
# for i in ["a","e","i","o","u"]:
#     string = string.replace("p"+i,"")
# print(string)

# 이거 틀림. 아무래도 글자 지운 후에 다시 p"ㅌ"꼴 글자가 있으면 그것이 남는듯.


# string = input()
#
# result = ""
# for i in string:
#     if i in ['a','e','i','o','u']:
#         result += i+"p"+i
#     else:
#         result += i
# print(result) # 이렇게 하면 창영이 일기 문장이 완성됨.

# 위 방법의 역으로 찾아내는 코드를 짜야됨.

string = input()

result = ""

idx = 0
while idx != len(string)-1:
    if string[idx] not in ['a','e','i','o','u']: # 모음이 아니라면 
        result += string[idx] # 그냥 더함
    else:
        if (string[idx+1] == 'p') and (string[idx +2] == string[idx]): # 모음이고 중간에 p가 있는거라면
            result += string[idx] # 해당 문자만 더하고
            idx += 1
    idx += 1
print(result)

# 위 코드도 틀림 =_=;; 근데 예제는 맞게 나옴.

## 다른 사람 코드 ##

sentence = input()
i = 0
vowels = ['a', 'e', 'i', 'o', 'u']
while i < len(sentence):    # for -> range error
    print(sentence[i], end='')
    if sentence[i] in vowels:
        i += 2
    i += 1




vowel_trans_li = ['apa','epe','ipi','opo','upu']
vowel = ['a','e','i','o','u']
sen = input()
for i in range(5):
    if vowel_trans_li[i] in sen:
        sen = sen.replace(vowel_trans_li[i], vowel[i])
print(sen)






diary = input()
i = 0
while i < len(diary):
    char = diary[i]
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(char, end="")
        i += 3
    else:
        print(char, end="")
        i += 1