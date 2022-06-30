

'''
문제를 보고 떠오른 생각은
2진 탐색으로 서치를 all 행, all 열 하면 될까? 싶음.

'''


class Solution:
    def binSearch(self, row, target):
        start = 0
        end = len(row)-1

        while start <= end:
            mid = (start+end)//2
            if target == row[mid]:
                return True
            elif target > row[mid]:
                start = mid+1
            else:
                end = mid-1
        return False

    def searchMatrix(self, matrix, target):
        for k in matrix: # 행 별로 이진탐색
            value = self.binSearch(k, target)
            if value == True:
                return True



matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

k = Solution()
print(k.searchMatrix(matrix, target))

# 옷? 바로 통과. 74번 문제도 비슷한 부류다.





### 책 풀이 ###

class Solution:
    def searchMatrix(self, matrix, target):
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로
            elif target > matrix[row][col]:
                row += 1
        return False





class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)
