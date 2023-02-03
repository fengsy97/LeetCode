 #
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (38.95%)
# Likes:    7897
# Dislikes: 541
# Total Accepted:    721K
# Total Submissions: 1.9M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
# 
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
# 
# Return intervals after the insertion.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start = 0
        end = len(intervals)-1
        while(start <= end):
            mid = int((end-start)/2) + start
            if(intervals[mid][1]<newInterval[0]):
                start = mid + 1
            else : end = mid - 1
        # print(start,end,mid)
        start_ = start
        start = 0
        end = len(intervals)-1
        while(start <= end):
            mid = int((end-start)/2) + start
            if(intervals[mid][0]<=newInterval[1]):
                start = mid + 1
            else : end = mid - 1
        end_ = end
        # print(start_,end_)
        if(start_ < len(intervals) and intervals[start_][0] <= newInterval[0]):
            newInterval[0] = intervals[start_][0]

        if(end >= 0 and intervals[end_][1] >= newInterval[1]):
            newInterval[1] = intervals[end_][1]
        # print(start_,end_)
        del intervals[start_:end_+1]
        intervals.insert(start_,newInterval)


        # print(start_,end_)
        return intervals

        
# @lc code=end

