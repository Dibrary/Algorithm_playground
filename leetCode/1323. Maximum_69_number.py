'''
6과 9로만 있는 숫자를 최대값으로 변경하기
'''


def test(num):
    num = str(num)
    six_cnt = 0
    nine_cnt = 0
    for i in num:
        if i == "6":  six_cnt += 1
        else:         nine_cnt += 1

    result = ""
    for j in range(nine_cnt):
        result += "9"
    for k in range(six_cnt):
        result += "6"

    return int(result)

'''
문제 이해를 잘못함.
딱 한개의 6만 9로 바꿀 수 있다. 최대값을 만들자.
'''

def test2(num):
    num = str(num)
    tmp = []

    flag = 0
    for i in num:
        if i == "6" and flag == 0:
            tmp.append("9")
            flag = 1
        else:
            tmp.append(i)

    result = ""
    for k in tmp:
        result += k

    return int(result)

if __name__=="__main__":
    print(test2("669966"))