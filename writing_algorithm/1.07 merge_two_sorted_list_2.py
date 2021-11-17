'''

정렬된 배열 num1, num2가 주어지고, 각각의 크기는 m 및 n이다.
정렬을 유지하면서 num1배열부터 채워나가 num2까지 확장해보자.
'''


def test(A, B):
    a_idx, b_idx = 0, 0

    while a_idx < len(A):
        print(a_idx)
        if A[a_idx] < B[b_idx]:
            a_idx += 1
            for i in range(0, len(A) - 1):  # 여기에 정렬을 직접 구현해 버렸다. (새로운 배열 안 씀)
                min_value = i
                for j in range(i + 1, len(A)):
                    if A[min_value] > A[j]:
                        min_value = j
                A[min_value], A[i] = A[i], A[min_value]
            pass

        elif A[a_idx] > B[b_idx]:

            A[a_idx], B[b_idx] = B[b_idx], A[a_idx]

            for i in range(0, len(B) - 1):  # 여기에 정렬을 직접 구현해 버렸다. (새로운 배열 안 씀)
                min_value = i
                for j in range(i + 1, len(B)):
                    if B[min_value] > B[j]:
                        min_value = j
                B[min_value], B[i] = B[i], B[min_value]

    return(A, B)

if __name__=="__main__":
    print(test([1,3,5,7],[2,4,8,10]))