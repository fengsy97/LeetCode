#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (56.73%)
# Likes:    18773
# Dislikes: 420
# Total Accepted:    2.1M
# Total Submissions: 3.6M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def find_land(self,x,y,grid):
        # print(x,y,grid[x][y])
        if(not grid[x][y] == "1"):return

        grid[x][y] = str(self.nums)
        for next in self.nexts:
            if(x+next[0]>=0 and x+next[0]<len(grid) and y+next[1]>=0 and y+next[1]<len(grid[0])):
                if(grid[x+next[0]][y+next[1]] == "1"):
                    self.find_land(x+next[0],y+next[1],grid)
        return


    def numIslands(self, grid: List[List[str]]) -> int:
        self.nexts = [[1,0],[-1,0],[0,1],[0,-1]]
        self.nums = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if(grid[i][j] == "1"):
                    # print(i,j,grid[i][j])
                    self.nums += 1
                    self.find_land(i,j,grid)
        return self.nums-2
# @lc code=end

