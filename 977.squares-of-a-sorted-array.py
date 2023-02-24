#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.91%)
# Likes:    7409
# Dislikes: 184
# Total Accepted:    1.3M
# Total Submissions: 1.9M
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
# 
# 
# 
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nag = []
        result = []
        while(nums):
            if nums[0] < 0: nag.insert(0,nums.pop(0))
            else:
                break
                
        # print(nums,nag) 
        i = j = 0
        while(i < len(nums) and j < len(nag)):
            if(nums[i]*nums[i] < nag[j]*nag[j]):
                result.append(nums[i]*nums[i])
                i+=1
            else:
                result.append(nag[j]*nag[j])
                j+=1
        while(i < len(nums)):
            result.append(nums[i]*nums[i])
            i+=1
        while(j < len(nag)):
            result.append(nag[j]*nag[j])
            j+=1
        return  result
# @lc code=end

