#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (58.18%)
# Likes:    13973
# Dislikes: 504
# Total Accepted:    1.3M
# Total Submissions: 2.3M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
# 
# You must solve this problem without using the library's sort function.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,0,1]
# Output: [0,1,2]
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# 
# 
# 
# Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        a = c = len(nums) - 1
        b = d = 0
        while(1):
            try:
                while(not nums[a] == 1):
                    a -= 1
            except:
                pass
            try:
                while(not nums[c] == 0):
                    c -= 1
            except:
                pass
            try:
                while(not nums[b] == 1):
                    b += 1
            except:
                pass
            try:
                while(not nums[d] == 2):
                    d += 1
            except:
                pass
            if(c > d):
                nums[c] = 2
                nums[d] = 0
            elif(a > d):
                nums[a] = 2
                nums[d] = 1
            elif(c > b):
                nums[c] = 1
                nums[b] = 0
            else:
                break
        
# @lc code=end

