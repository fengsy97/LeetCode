#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.85%)
# Likes:    8687
# Dislikes: 466
# Total Accepted:    995.7K
# Total Submissions: 2.2M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def find(self,nums,target):
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = int((end - start)/2) + start
            if(nums[mid] < target):
                start = mid + 1
            else:
                end = mid - 1
        return end
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sorted(nums)
        nums.sort()
        print(nums)
        result = 999999
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                # print(target - nums[i] - nums[j])
                rank = self.find(nums,target - nums[i] - nums[j])
                if(rank >= 0 and rank < len(nums) and (not rank == i) and (not rank == j)):
                    if(abs(result - target) > abs(target - nums[rank] - nums[i] - nums[j])):result = nums[rank] + nums[i] + nums[j]
                rank+=1
                if(rank >= 0 and rank < len(nums) and (not rank == i) and (not rank == j)):
                    if(abs(result - target) > abs(target - nums[rank] - nums[i] - nums[j])):result = nums[rank] + nums[i] + nums[j]
                # print(i,j,rank,target,target - nums[i] - nums[j])
        # if(result = )
        return result

# @lc code=end

