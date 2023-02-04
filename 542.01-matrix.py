#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (44.49%)
# Likes:    6487
# Dislikes: 312
# Total Accepted:    351.8K
# Total Submissions: 790.7K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
# 
# 0 -> -1
# 1 -> -2
# x -> -x - 1

# @lc code=start
# def bfs(i,j,mat,mark):
    # # print(i,j)
    # if(mark[i][j] == 1): return mat[i][j]
    # mark[i][j] = 1
    # if(mat[i][j] == 0):
    #     # mark[i][j] = 1
    #     return 0
    # else:
    #     if(i>0):
    #         if(mat[i-1][j] == 0):
    #             mark[i-1][j] = 1
    #             # mark[i][j] = 1
    #             mat[i][j] = 1
    #             return 1    
    #     if(j>0):
    #         if(mat[i][j-1] == 0):
    #             mark[i][j-1] = 1
    #             # mark[i][j] = 1
    #             mat[i][j] = 1
    #             return 1       
    #     if(i<len(mat)-1):
    #         if(mat[i+1][j] == 0):
    #             mark[i+1][j] = 1
    #             # mark[i][j] = 1
    #             mat[i][j] = 1
    #             return 1           
    #     if(j<len(mat[0])-1):
    #         if(mat[i][j+1] == 0):
    #             mark[i][j+1] = 1
    #             # mark[i][j] = 1
    #             mat[i][j] = 1
    #             return 1

        # print(i,j,min_temp)
        # min_temp = 99999
        # if(i>0): if(mark[i][j] == 1):min_temp = min(min_temp,bfs(i-1,j,mat,mark))
        # print(i,j,min_temp)
        # if(j>0):min_temp = min(min_temp,bfs(i,j-1,mat,mark))
        # print(i,j,min_temp)
        # if(i<len(mat)-1):min_temp = min(min_temp,bfs(i+1,j,mat,mark))
        # print(i,j,min_temp)
        # if(j<len(mat[0])-1):min_temp = min(min_temp,bfs(i,j+1,mat,mark))
        # # mark[i][j] = 1
        # mat[i][j] = min_temp + 1
        # print(i,j,min_temp)
        # return min_temp+1
             


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        # mark = [[100000]*n for i in range(m)]
        task_queue = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] == 0):
                    task_queue.append([i,j])
                else:
                    mat[i][j] = 100000
        while(task_queue):
            [i,j] = task_queue.pop(0)
            # mark[i][j] = 1
            # if(not mat[i][j] == 100000): continue
            if(mat[i][j] == 0) :
                mat[i][j] = 0
            else:
                # print(i,j)
                min_temp = 99999
                if(i > 0):min_temp = min(min_temp,mat[i-1][j])
                if(j > 0):min_temp = min(min_temp,mat[i][j-1])
                if(i < len(mat) - 1):min_temp = min(min_temp,mat[i+1][j])
                if(j < len(mat[0]) - 1):min_temp = min(min_temp,mat[i][j+1])
                mat[i][j] = min_temp + 1
            
            if(i>0):
                if( mat[i-1][j] == 100000):
                    task_queue.append([i-1,j])
            if(j>0):
                if( mat[i][j-1] == 100000):
                    task_queue.append([i,j-1])
            if(i < len(mat) - 1):
                if( mat[i+1][j] == 100000):
                    task_queue.append([i+1,j])
            if(j < len(mat[0]) - 1):
                if( mat[i][j+1] == 100000):
                    task_queue.append([i,j+1])
        return mat
                    
# @lc code=end

