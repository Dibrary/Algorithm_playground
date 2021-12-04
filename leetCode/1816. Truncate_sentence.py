'''
입력 숫자 만큼의 단어만 내보내기
'''

def test(s, k):
    tmp = list(s.split(" "))
    result = ""
    for idx, i in enumerate(tmp):
        print(idx)
        if idx == k-1:
            result += i
            break
        else:
            result += i +" "

    return result

if __name__=="__main__":
    print(test("Hello how are you Contestant", 4))
    print(test("What is the solution to this problem", 4))