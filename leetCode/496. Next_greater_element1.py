nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]

result = []
for i in nums1:
    idx = nums2.index(i)

    if idx == len(nums2) - 1:
        result.append(-1)
    elif nums2[idx + 1] > nums2[idx]:
        result.append(nums2[idx + 1])
    else:
        if max(nums2[idx:]) > nums2[idx]:
            result.append(max(nums2[idx:]))
        else:
            flag = 0
            for j in nums2[idx:]:
                if j > i:
                    result.append(j)
                    flag = 1
                    break
            if flag == 0:
                result.append(-1)
print(result)# 실패


