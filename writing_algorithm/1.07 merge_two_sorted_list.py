'''

정렬된 배열 num1, num2가 주어지고, 각각의 크기는 m 및 n이다.
정렬을 유지하면서 num1배열부터 채워나가 num2까지 확장해보자.
'''


def test(A, B):
    a_idx, b_idx = 0, 0

    while a_idx < len(A):
        if A[a_idx] < B[b_idx]:
            a_idx += 1
            pass
        elif A[a_idx] > B[b_idx]:
            A[a_idx], B[b_idx] = B[b_idx], A[a_idx]
            B = sorted(B)  # 이걸 배열을 새로 생성한 것으로 볼 수 있다.
    return(A, B)

if __name__=="__main__":
    print(test([1,3,5,7],[2,4,8]))