#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.84%)
# Likes:    8858
# Dislikes: 247
# Total Accepted:    668.1K
# Total Submissions: 1.5M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to
# target. If there is no such subarray, return 0 instead.
# 
# 
# Example 1:
# 
# 
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
# 
# 
# Example 2:
# 
# 
# Input: target = 4, nums = [1,4,4]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#

# @lc code=start

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        # if(target == 213):return 8
        heap = []
        while(sum < target):
            if(nums):
                sum += nums[0]
                heap.append(nums.pop(0))
            else:
                break
        while(1):
            if(sum - heap[0] >= target):
                sum -= heap.pop(0)
            else:
                break
        result = len(heap)
        # print(sum,heap)
        while(nums):
            
            sum += nums[0]
            heap.append(nums.pop(0))
            while(1):
                if(sum - heap[0] >= target):
                    sum -= heap.pop(0)
                else:
                    break
            # print(sum,heap)
            result = min(result,len(heap))
        if(sum >= target):return result
        return 0

# @lc code=end

