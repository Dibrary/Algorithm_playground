'''
matrix가 주어질 때,
대각선 값만 모두 더한 값을 출력하는 코드를 만들자.
'''

class Solution:
    def diagonalSum(self, mat):
        first = 0
        last = len(mat)-1
        result = 0

        for i in range(0, len(mat)):
            if first == last and mat[i][first] == mat[i][last]:
                result += mat[i][first]
                first += 1
                last -= 1
            else:
                result += mat[i][first]
                result += mat[i][last]
                first += 1
                last -= 1
        return result

    def diagonalSum2(self, mat):
        first = 0
        result = 0

        for i in range(0, len(mat)):
            if first == len(mat)-1-first:
                result += mat[i][first]
                first += 1
            else:
                result += mat[i][first]
                result += mat[i][len(mat)-1-first]
                first += 1
        return result


if __name__=="__main__":
    k = Solution()
    print(k.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(k.diagonalSum2([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))