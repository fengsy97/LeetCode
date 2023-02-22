#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (46.83%)
# Likes:    6198
# Dislikes: 247
# Total Accepted:    290.8K
# Total Submissions: 621K
# Testcase Example:  '[0,1]'
#
# Given a binary array nums, return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number
# of 0 and 1.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        count = {}
        num = 0
        count[0] = -1
        for i in range(len(nums)):
            if(nums[i]):num += 1
            else: num -= 1
            if(num in count):
                result = max(result, i - count[num])
                # if(i - count[num] > result):result =
            else:
                count[num] = i
        return result
# @lc code=end

