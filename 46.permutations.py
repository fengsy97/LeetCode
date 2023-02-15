#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (75.33%)
# Likes:    14675
# Dislikes: 251
# Total Accepted:    1.5M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def find(self,remains,result):
        temp_re = remains.copy()
        temp_result = result.copy()
        for i in range(len(remains)):
            temp_result.append(temp_re.pop(i))
            if(not temp_re):
                self.results.append(temp_result)
                return
            self.find(temp_re,temp_result)
            temp_re.insert(i,temp_result.pop())

                

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.find(nums,[])
        return self.results
        
# @lc code=end

