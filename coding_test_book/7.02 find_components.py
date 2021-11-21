'''
N개의 부품 재고가 있다.
그리고 N개의 부품 재고마다 고유 번호가 있다.

M개의 부품 요청이 있을 때,
M개 고유 번호가 N개 재고 안에 있는지 여부를 반환하자.
'''

def receive_func():
    print("부품 재고 갯수를 입력하세요.")
    n = int(input())
    n_list = []
    print("부품 고유 넘버를 입력해 두세요.")
    for i in range(0, n):
        n_list.append(int(input()))

    print("소비자 요청 부품 갯수를 입력하세요.")
    m = int(input())
    m_list = []
    print("소비자 요청 부품 고유 넘버를 입력해 두세요.")
    for i in range(0, m):
        m_list.append(int(input()))
    return n_list, m_list

def test():
    n_list, m_list = receive_func()
    for i in m_list:
        if i in n_list:  print("yes", end=' ')
        else:            print("no", end=' ')

if __name__=="__main__":
    test()




