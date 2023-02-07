#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (45.36%)
# Likes:    12635
# Dislikes: 491
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start




class Solution:
    def judge(self,i,fathers):
        self.visit.add(i)
        for require in self.requirelist[i]:
            # print("require add ", require)
            self.cout.add(require)
            if require in fathers:return False
        fathers.append(i)
        for require in self.requirelist[i]:
            if(not require in self.visit):
                if(not self.judge(require,fathers)):return False
        fathers.pop()
        return True
            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print("test")
        self.requirelist = [[]for i in range(numCourses)]
        for c1, c2 in prerequisites:
            self.requirelist[c2].append(c1)
        # print(self.requirelist) 
        self.hash_table = []
        self.cout = set()
        self.visit = set()
        
        for i in range(numCourses):
            
            if(not self.requirelist[i]): continue
            if(i in self.cout):continue
            print(i)
            self.hash_table.clear()
            self.hash_table.append(i)
            self.visit.clear()
            if(not self.judge(i,self.hash_table)):
                return False
        return True
            # for require in self.requirelist[i]:
                  


        
# @lc code=end

