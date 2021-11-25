'''
kakao 2018 blind
'''

def solution(dartResult):
    tmp_idx = 0

    result = []
    dartResult += "0" # 숫자 앞을 기준으로 자르기 때문에, 맨 마지막 값이 안 들어감, 처리를 위해 임시로 계산 (끝에 주어진 값이 숫자라 하더라도, 괜찮다)
    for idx, i in enumerate(dartResult):
        if idx != 0 and i.isdigit():
            result.append(dartResult[tmp_idx:idx])
            tmp_idx = idx
    print(result) # 분리하는 데 까지는 성공.




if __name__=="__main__":
    solution("1S*2T*3S9")
    
# 제일 먼저 든 생각은 숫자 앞을 기준으로, 띄워놔야 한다는 생각

