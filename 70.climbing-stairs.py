#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (52.15%)
# Likes:    16978
# Dislikes: 519
# Total Accepted:    2.2M
# Total Submissions: 4.2M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):return 1
        ans = [1,2]
        for i in range(2,n):
            ans.append(ans[i-1] + ans[i-2])
        return ans[-1]
# @lc code=end

