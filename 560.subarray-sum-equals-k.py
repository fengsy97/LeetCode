#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.77%)
# Likes:    17284
# Dislikes: 505
# Total Accepted:    935.4K
# Total Submissions: 2.1M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        result = 0
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if(temp == k):result += 1
            if(temp - k in count):result += count[temp - k]
            if temp in count:
                count[temp] += 1
            else: count[temp] = 1
        return result
        
# @lc code=end

