'''
두 개의 연결 리스트로 표현된 숫자를 더하고,
더한 값을 다시 연결 리스트로 만들어서 반환하자.
'''

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def value_parsing(num1, num2): # 연결 리스트의 value만 가져오는 코드 분리
    first=''; second=''
    while num1 != None:
        first += str(num1.val)
        num1 = num1.next

    while num2 != None:
        second += str(num2.val)
        num2 = num2.next
    return first, second

def test(num1, num2): # 각 값의 root가 들어온다.
    first, second = value_parsing(num1, num2)

    # result = list(str(int(first) + int(second))) # int로 더하고, str로 바꿔서 다시 잘라냄.
    result = [int(k) for k in str(int(first) + int(second))]

    root = None
    result_root = None # 반환용 처음 노드 저장 변수.
    for i in range(0, len(result)):
        if i == 0:
            root = Node(result.pop(0))
            result_root = root
        else:
            root.next = Node(result.pop(0))
            root = root.next

    return result_root

if __name__=="__main__":
    t1 = Node(9, None)
    s1 = Node(4, t1)
    f1 = Node(1,s1) # 즉 이 수는 149

    s3 = Node(2, None)
    t2 = Node(9, s3)
    s2 = Node(7, t2)
    f2 = Node(5, s2) # 즉 이 수는 5792

    st = test(f1, f2)

    while st != None:
        print(st.val, end=' ') # 5941이 나와야 함.
        st = st.next
