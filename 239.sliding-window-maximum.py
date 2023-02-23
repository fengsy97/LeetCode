#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (46.39%)
# Likes:    13724
# Dislikes: 444
# Total Accepted:    726.8K
# Total Submissions: 1.6M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        values = []
        ranks = []
        for i in range(len(nums)):
            if (not values):
                values.append(nums[i])
                ranks.append(i)
                if(i+1 >= k):result.append(values[0])
                continue
            if(i - k == ranks[0]):
                ranks.pop(0)
                values.pop(0)
            if (not values):
                values.append(nums[i])
                ranks.append(i)
                if(i+1 >= k):result.append(values[0])
                continue
            # print(values,i,nums[i])
            if(values[0] <= nums[i]):
                values.clear()
                ranks.clear()
                values.append(nums[i])
                ranks.append(i)
            else:
                while(values[-1] <= nums[i]):
                    ranks.pop()
                    values.pop()
                values.append(nums[i])
                ranks.append(i)

            if(i+1 >= k):result.append(values[0])
        return result

# @lc code=end

