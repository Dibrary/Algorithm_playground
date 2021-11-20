'''
성적이 낮은 학생의 이름이 리스트에 맨 앞에서 출력되게 하자.
'''

def test():
    print("갯수를 입력하세요")
    n = int(input())
    print("학생의 이름과 값을 입력하세요.")
    nums = []
    for k in range(0, n):
        name, score = input().split()
        nums.append((name, int(score)))

    nums.sort(key=(lambda x: x[1]))

    for i in nums:
        print(i[0], end=' ')

if __name__=="__main__":
    test()


