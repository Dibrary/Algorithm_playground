
def solution(numbers):
    arr = []
    for i in numbers:
        arr.append([int(x) for x in str(i)])

    result = ""

    while arr:
        arr.sort(key=lambda x: -x[0])
        if arr[0][0] != arr[1][0]:
            result += str(arr[0][0])
            arr.pop(0)
        else:
            break
        # 근데 길이가 같을지, 다를지에 대해 미리 정할 수 없는거 같은데;;
    return result


print(solution([3,30,34,5,9]))



