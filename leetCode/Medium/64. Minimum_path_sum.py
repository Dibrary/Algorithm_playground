class Solution:
    def upline(self, grid):
        total = 0
        total += sum(grid[0])

        for i in range(1, len(grid)):
            total += grid[i][-1]
        return total

    def downline(self, grid):
        total = 0
        total += sum(grid[len(grid) - 1])

        for k in range(0, len(grid) - 1):
            total += grid[k][0]
        return total

    def minPathSum(self, grid):
        return min(self.upline(grid), self.downline(grid))

# 이렇게 했는데 실패
# 전체 경로 중에 최소를 찾아야 됨. (BFS를 써야 하는 듯 싶다)