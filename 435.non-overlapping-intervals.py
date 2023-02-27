#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (50.14%)
# Likes:    5519
# Dislikes: 155
# Total Accepted:    344.5K
# Total Submissions: 686.7K
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# 
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def find(self,intervals,pos):
        
        if(pos == len(intervals) - 1):
            if(len(intervals) > self.remain):self.remain = len(intervals)
            return
        if(len(intervals) <= self.remain):return
        if(tuple(intervals[pos]) in self.judge):
            if(pos < self.judge[tuple(intervals[pos])]):
                # print(pos,self.judge[tuple(intervals[pos])],tuple(intervals[pos]))
                return
            else:
                self.judge[tuple(intervals[pos])] = pos
        else:
            self.judge[tuple(intervals[pos])] = pos
            # print(pos,tuple(intervals[pos]))
        if(intervals[pos][1]>intervals[pos+1][0]):
            temp = intervals[pos]
            intervals.pop(pos)
            self.find(intervals,pos)
            intervals.insert(pos,temp)
            # next = 1 + pos
            temp = []
            while(pos < len(intervals) - 1 and intervals[pos][1]>intervals[pos+1][0]):
                temp.append(intervals.pop(pos+1))
            # temp = intervals[pos+1]
            # intervals.pop(pos+1)
            self.find(intervals,pos+1)
            while(temp):
                intervals.insert(pos+1,temp.pop())
        else:
            self.find(intervals,pos+1)
        return
        
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0],interval[1]))
        max_len  = len(intervals)
        self.judge = {}
        self.remain  = 0
        self.find(intervals,0)
        # print(intervals)
        return max_len - self.remain
# @lc code=end

