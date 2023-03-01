#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (60.84%)
# Likes:    2870
# Dislikes: 50
# Total Accepted:    82.6K
# Total Submissions: 135.6K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in non-decreasing order. Find the
# smallest range that includes at least one number from each of the k lists.
# 
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a
# < c if b - a == d - c.
# 
# 
# Example 1:
# 
# 
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# 
# 
# Example 2:
# 
# 
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
# 
# 
# 
# Constraints:
# 
# 
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10^5 <= nums[i][j] <= 10^5
# nums[i] is sorted in non-decreasing order.
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def judge(self,result1,result2):
        if(result1[1] - result1[0] > result2[1] - result2[0]):return result2
        elif(result1[1] - result1[0] < result2[1] - result2[0]):return result1
        else:
            if(result1[0] < result2[0]):return result1
            else:return result2
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if(len(nums) == 1):return [nums[0][0],nums[0][0]]
        maxnum = -500000
        maxlist = set()
        heap = []
        empty = 0
        result = [0,9000000]
        for i in range(len(nums)):
            if(maxnum < nums[i][0]):
                maxnum = nums[i][0]
                # maxlist.clear
                # maxlist.add(i)
            heapq.heappush(heap,(nums[i].pop(0),i))
        while(not empty):
            
            start,i = heapq.heappop(heap)
            end = maxnum
            result = self.judge(result,[start,end])
            # nums[i].pop(0)
            if(nums[i]):
                if(maxnum < nums[i][0]):
                    maxnum = nums[i][0]
                heapq.heappush(heap,(nums[i].pop(0),i))
            else:
                empty = 1
            # print(result)
        return result

        
# @lc code=end

