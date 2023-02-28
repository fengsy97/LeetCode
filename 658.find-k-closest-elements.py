#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (46.79%)
# Likes:    6698
# Dislikes: 542
# Total Accepted:    417.7K
# Total Submissions: 892.7K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.
# 
# An integer a is closer to x than an integer b if:
# 
# 
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
# 
# 
# 
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
# 
# 
# Constraints:
# 
# 
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def find(self,nums,target):
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = int((end - start) / 2) + start
            if(nums[mid] < target):
                start = mid + 1
            else:
                end = mid -1
        return end
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = self.find(arr,x)
        right = left+1
        left_offset = right_offset = 0
        result = []
        while(left >= 0 and left < len(arr) and right >= 0 and right < len(arr) and k > 0):
            left_offset = abs(x - arr[left])
            right_offset = abs(x - arr[right])
            if(left_offset <= right_offset):
                result.insert(0,arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            k -= 1
        # print(result,left,right,k)
        while(left >= 0 and left < len(arr) and k>0):
            result.insert(0,arr[left])
            left -= 1
            k -= 1
        # print(result,left,right,k)
        while(right >= 0 and right < len(arr) and k>0):
            result.append(arr[right])
            right += 1
            k -= 1
        # print(result,left,right)
        return result

            
# @lc code=end

