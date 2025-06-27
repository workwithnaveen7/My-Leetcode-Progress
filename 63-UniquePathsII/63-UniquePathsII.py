# Last updated: 6/27/2025, 10:21:18 AM
class Solution:
    def utility(self,grid, i, j, m, n,table):
        if (i>=m or j>=n):
            return 0
        if (grid[i][j]==1):
            return 0
        if (i==m-1 and j ==n-1):
            return 1
        if (table[i][j]!=-1):
            return table[i][j]

        table[i][j]=self.utility(grid, i+1,j,m,n,table)+self.utility(grid,i,j+1,m,n,table)
        return table[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        table = [[-1 for _ in range(n)] for _ in range(m)] 
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        return self.utility(obstacleGrid,0,0,m,n,table)

    


        