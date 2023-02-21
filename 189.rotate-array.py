#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Medium (39.33%)
# Likes:    13187
# Dislikes: 1547
# Total Accepted:    1.4M
# Total Submissions: 3.6M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an integer array nums, rotate the array to the right by k steps, where
# k is non-negative.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# Try to come up with as many solutions as you can. There are at least three
# different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
# 
#

# @lc code=start

def hcf(x, y):
 
   # 获取最小值
   if x > y:
       smaller = y
   else:
       smaller = x
 
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
 
   return hcf

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if(not k):return None
        n = hcf(len(nums),k)
        if(not n):
            pos = 0
            next_pos = (k)%len(nums)
            for i in range(len(nums)-1):
                temp = nums[pos]
                nums[pos] = nums[next_pos]
                nums[next_pos] = temp
                next_pos += k
                next_pos = next_pos%len(nums)
                print(nums)
                
        else:
            times = int(len(nums)/n)
            for j in range(n):
                pos = j
                next_pos = (pos+k)%len(nums)
                # temp = nums[pos]
                for i in range(times):
                    temp = nums[pos]
                    nums[pos] = nums[next_pos]
                    nums[next_pos] = temp
                    next_pos += k
                    next_pos = next_pos%len(nums)
                    # if pos >= len(nums):pos -= len(nums)


        
# @lc code=end

