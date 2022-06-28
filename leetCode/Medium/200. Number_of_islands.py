import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)


class Solution:
    def __init__(self):
        self.visited = None

    def dfs(self, y, x, grid):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or self.visited[y][x] == 1 or grid[y][x] == "0": # 여기서 y<0 or x<0 or y>=len(grid) or x>=len(grid[0]) 이게 먼저 나오지 않으면 이러 남.
            return False
        self.visited[y][x] = 1
        self.dfs(y - 1, x, grid)
        self.dfs(y, x - 1, grid)
        self.dfs(y + 1, x, grid)
        self.dfs(y, x + 1, grid)
        return True

    def numIslands(self, grid):
        self.visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.visited[i][j] == 0 and grid[i][j] == "1":
                    value = self.dfs(i, j, grid)
                    if value:
                        cnt += 1
        return cnt


grid = [["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]]
k = Solution()

k.numIslands(grid)


### 책 풀이 코드 ###

class Solution:
    def numIslands(self, grid):
        def dfs(i, j): # 중첩 함수 사용. 중첩함수는 부모함수에서 선언한 변수도 유효 범위에서 사용 가능.
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


