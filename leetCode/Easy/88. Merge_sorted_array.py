'''
두 리스트의 값 하나로 합치기
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in nums2:
            nums1[m] = i
            m += 1
        nums1.sort()

        # 처음에 막 일일이 값을 떼내고 합하고 하려고 했음.
        # result = []
        # num1_start_idx, num1_end_idx = 0, m-1
        # num2_start_idx, num2_end_idx = 0, n-1
        #
        # for i in range(0, m+n):
        #     if num1[num1_start_idx] == 0:
        #         num1_start_idx += 1
        #         continue
        #     if num2[num2_start_idx] == 0:
        #         num2_start_idx += 1
        #         continue
        #
        #     if num1[num1_start_idx] > num2[num2_start_idx]:
        #         result.append(num2[num2_start_idx])
        #         num2_start_idx += 1
        #     elif num1[num1_start_idx] > num2[num2_start_idx]:
        #         result.append(num1[num1_start_idx])
        #         num1_start_idx += 1
        # return result
        return nums1 # 단순 확인용.

if __name__=="__main__":
    k = Solution()
    print(k.merge([1,3,5,7,0,0], 4 ,[6,8], 2))

