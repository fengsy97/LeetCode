#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (48.64%)
# Likes:    14994
# Dislikes: 624
# Total Accepted:    1M
# Total Submissions: 2.1M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def find(self,set_,num):
        result = 1
        temp = num
        while(num+1 in set_):
            result += 1
            num += 1
            set_.remove(num)
        while(temp - 1 in set_):
            result += 1
            temp -= 1
            set_.remove(temp)
        return result

    def longestConsecutive(self, nums: List[int]) -> int:
        table = set()
        for num in nums:
            table.add(num)
        print(table)
        result = 0
        while(table):
            num = table.pop()
            result = max(result,self.find(table,num))
        return result
        
# @lc code=end

