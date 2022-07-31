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


#### 다른 사람 풀이 #####

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0') # rjust는 오른쪽으로 정렬해서 보기좋게 출력할 때 씀.
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

##############################
import re

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer
