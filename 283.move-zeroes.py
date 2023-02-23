#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (61.40%)
# Likes:    12785
# Dislikes: 324
# Total Accepted:    2.1M
# Total Submissions: 3.5M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos0=pos1=0
        while(not nums[pos1]):
            if(pos1+1 == len(nums)):return
            pos1+=1
        while(nums[pos0]):
            if(pos0+1 == len(nums)):break
            pos0 += 1
        while(pos1 < len(nums) and pos0 < len(nums)):
            # print(pos1,pos0)
            if(pos1 > pos0):
                nums[pos0] = nums[pos1]
                nums[pos1] = 0
                if(pos0+1 == len(nums)):return
                pos0+= 1
            if(pos1+1 == len(nums)):return
            pos1+= 1
            
            while(not nums[pos1]):
                if(pos1+1 == len(nums)):return
                pos1 +=1
            while(nums[pos0]):
                if(pos0+1 == len(nums)):break
                pos0 += 1

        
# @lc code=end

