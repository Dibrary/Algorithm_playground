
n = int(input())

for idx, s in enumerate(range(n)):
    string = "".join(map(str,sorted(str(s),reverse=True)))
    print(s, string, idx)
    '''
    여기에서 숫자가 같은게 없는지 체크 함수 필요
    
    '''

    if str(s) == string:
        print(s, idx, "해당됨")