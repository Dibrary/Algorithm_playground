
'''
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하기.

2개의 포인터를 쓴다면,
시작부, 옆부 옆부가 시작부 높이보다 높으면 시작부를 옆부로 갱신한다.
옆부가 시작부보다 낮으면 그 숫자 차이 만큼을 + 해 놓는다.
'''

# class Solution:
#     def trap(self, height):
#         start_idx = 0
#         end_idx = 1
#         result = 0
#
#         while end_idx < len(height):
#             if height[start_idx] < height[end_idx]:
#                 start_idx = end_idx
#                 end_idx += 1
#             elif height[start_idx] > height[end_idx]:
#                 result += height[start_idx] - height[end_idx]
#                 end_idx += 1
#         return result
#
#
# k = Solution()
# print(k.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# 그냥 위 처럼 하면 결과가 11이 나오는데, 이는 3을 기준으로 오른쪽이 모조리 '물이 찬다'로 계산되기 때문.



# 단순히 2개만을 비교하지 말고, 더 높은게 있는 경우에만 +를 하게 바꿔보자.

# class Solution:
#     def trap(self, height):
#         start_idx = 0
#         if height == [0]: # 이런 거지같은 input이 있다 =_=;;
#             return 0
#
#         while True:
#             if height[start_idx] == 0:
#                 start_idx += 1
#             else:
#                 break
#
#         end_idx = start_idx + 1
#         result = 0
#
#         max_value_idx = height.index(max(height))
#
#         while end_idx < len(height):
#             if height[end_idx] >= height[start_idx]:
#                 for k in range(start_idx+1, end_idx):
#                     result += height[start_idx] - height[k]
#                 start_idx = end_idx
#                 end_idx += 1
#             else:
#                 if start_idx == max_value_idx and height.count(height[max_value_idx]) == 1:
#                     start_idx += 1
#                 end_idx += 1
#         return result
#
#
# k = Solution()
# print(k.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 이게 6이 나와야 되는데 9가 나옴.
# print(k.trap([4,2,0,3,2,5])) # 이건 정상으로 나옴.

# print(k.trap([2,0,2])) # 출력이 2가 나와야 하는데 0이 나옴.
# print(k.trap([4,2,3])) # 출력이 1이 나와야 하는데 0이 나옴.





### 책 풀이 ###

class Solution:
    def trap(self, height):
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right: # 최대 높이 막대 까지 좌우 기둥 최대 높이값(_max)이 현재 높이와의 차이 만큼 volume을 더해간다.
            # 최대 지점에서 left, right가 만난다. while 탈출.
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            print(left_max, height[left], right_max, height[right], volume)
            # 낮은 쪽은 높은쪽을 향해 포인터가 이동한다.

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1 # 오른쪽이 크다면 왼쪽이 오른쪽으로 이동,
            else:
                volume += right_max - height[right]
                right -= 1 # 왼쪽이 크다면 오른쪽이 왼쪽으로 이동,
        return volume

k = Solution()
print(k.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

'''
위 예제 print(left_max, height[left], right_max, height[right], volume) 코드로 살펴보면
출력은 이렇다.

0 0 1 1 0
1 1 1 1 0
1 0 1 1 0
2 2 1 1 1
2 2 2 2 1
2 1 2 2 1
2 0 2 2 2
2 1 2 2 4
3 3 2 2 5
3 3 2 1 5
3 3 2 2 6
'''


### 스택 사용한 책 풀이 ###

# class Solution:
#     def trap(self, height):
#         stack = []
#         volume = 0
#
#         for i in range(len(height)):
#             while stack and height[i] > height[stack[-1]]: # 현재 높이가 이전 높이보다 높을 때, 그 격차 만큼의 물높이를 채운다.
#                 top = stack.pop()
#                 if not len(stack):
#                     break
#
#                 distance = i - stack[-1] -1
#                 waters = min(height[i], height[stack[-1]]- height[top])
#
#                 volume += distance * waters
#             stack.append(i)
#         return volume


### 다른 사람 코드 ###

class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0

        ans = 0

        while left <= right:
            if left_max <= right_max:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1

        return ans


class Solution:
    def trap(self, height):
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                curr = stack.pop()
                if not stack:
                    break
                base = i - stack[-1] - 1
                high = min(height[i], height[stack[-1]]) - height[curr]
                res += base * high
            stack.append(i)
        return res