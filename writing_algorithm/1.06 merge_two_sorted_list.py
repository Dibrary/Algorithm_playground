'''
Merge two sorted list.

in merging, Must be sustain sorting situation.
'''


def test():
    print("input the first list(num1)(it must be longer than num2")
    num1 = [int(x) for x in input().split()]
    print("input the second list(num2)")
    num2 = [int(y) for y in input().split()]

    if num2 == []:
        return num1

    idx_1 = 0
    idx_2 = 0

    while idx_1 != len(num1):
        if num1[idx_1] < num2[idx_2] and num1[idx_1] != 0:
            idx_1 += 1
        elif num1[idx_1] > num2[idx_2]:
            num2[idx_2], num1[idx_1] = num1[idx_1], num2[idx_2]
            num2 = sorted(num2)
        elif num1[idx_1] == num2[idx_2]:
            idx_1 += 1
        else:
            num2[idx_2], num1[idx_1] = num1[idx_1], num2[idx_2]
            idx_2 += 1
            idx_1 += 1
    return num1

if __name__=="__main__":
    print(test())





