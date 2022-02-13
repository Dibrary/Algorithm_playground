
def duplicateZeros(arr):

    result = []

    for i in range(0, len(arr)):
        if i == 0:
            if arr[i] == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(arr[i])
        else:
            if arr[i] == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(arr[i])
        if len(result) == len(arr):
            break
    print(result)


duplicateZeros([1,2,3])

# 근데 inplace로 해야 한다.

