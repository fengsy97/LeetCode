#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (52.76%)
# Likes:    9651
# Dislikes: 331
# Total Accepted:    557.8K
# Total Submissions: 1.1M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
# 
# 
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
# 
# 
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.remain = set()
        self.rot = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    self.rot.append((i,j))
                elif(grid[i][j] == 1):
                    self.remain.add((i,j))
        self.nums = 3
        self.nexts = [[1,0],[-1,0],[0,1],[0,-1]]
        # if(not self.remain):return 0
        while(self.rot and self.remain):
            # print(self.rot)
            # print(self.remain)
            length = len(self.rot)
            self.nums += 1
            for i in range(length):
                x,y = self.rot.pop(0)
                grid[x][y] = self.nums
                for next in self.nexts:
                    if (x+next[0],y+next[1]) in self.remain:
                        self.rot.append((x+next[0],y+next[1]))
                        self.remain.remove((x+next[0],y+next[1]))
            # print(self.rot)
            # print(self.remain)
        if(self.remain): return -1
        return self.nums-3
# @lc code=end

