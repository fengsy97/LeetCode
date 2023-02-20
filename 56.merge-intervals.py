#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (46.09%)
# Likes:    18075
# Dislikes: 620
# Total Accepted:    1.8M
# Total Submissions: 3.9M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def find(self,intervals,target):
        start = 0
        end = len(intervals)  - 1
        while(start <= end):
            mid = int((end - start)/2) + start
            if(intervals[mid][0] <= target[1]):
                start = mid + 1
            else:
                end = mid - 1
        return end
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorted(intervals, key=lambda interval: interval[0])
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        # print(self.find(intervals,intervals[2]))
        result = []
        result.append(intervals.pop(0))
        while(intervals):
            target = result.pop()

            # rank = self.find(intervals,target)
            # print(intervals,rank,target)
            
            if(target[1]>=intervals[0][0]):
                # temp = 
                result.append([target[0],max(target[1],intervals[0][1])])
                intervals.pop(0)
            else:
                result.append(target)
                result.append(intervals.pop(0))
        return result
# @lc code=end

