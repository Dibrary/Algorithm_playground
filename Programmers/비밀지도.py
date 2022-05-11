# n은 숫자
# arr1은 리스트 [9,20,28,18,11]
# arr2는 리스트 [30,1,21,17,28]

def make_binArray(n, arr):
    tmp = []

    for i in arr:
        bin_value = bin(i)[2:]
        tmp.append(list((n - len(bin_value)) * "0" + bin_value))

    return tmp


def add_binArray(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        tmp = ''
        for j in range(len(arr1[0])):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                tmp += '#'
            else:
                tmp += " "
        result.append(tmp)
    return result


def solution(n, arr1, arr2):
    tmp1 = make_binArray(n, arr1)
    tmp2 = make_binArray(n, arr2)

    answer = add_binArray(tmp1, tmp2)
    return answer
