#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (56.20%)
# Likes:    7990
# Dislikes: 1592
# Total Accepted:    414.1K
# Total Submissions: 736.7K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any
# order. Each task is done in one unit of time. For each unit of time, the CPU
# could complete either one task or just be idle.
# 
# However, there is a non-negative integer n that represents the cooldown
# period between two same tasks (the same letter in the array), that is that
# there must be at least n units of time between any two same tasks.
# 
# Return the least number of units of times that the CPU will take to finish
# all the given tasks.
# 
# 
# Example 1:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# 
# 
# Example 2:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# 
# 
# Example 3:
# 
# 
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle
# -> idle -> A
# 
# 
# 
# Constraints:
# 
# 
# 1 <= task.length <= 10^4
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if(not n):return len(tasks)
        count = {}
        for letter in tasks:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        heap = []
        result = []
        time = 0
        for key in count:
            heapq.heappush(heap,-count[key])
        n += 1
        offset = 0
        tomin = 0 
        # print(heap)
        while(heap):
            
            # print(result)
            while(len(result) < n and heap):
                num = heapq.heappop(heap)
                result.append(-num)
            # if(heap):tomin = -heap[0] - 1
            # else : tomin = result[-1]
            tomin = 1
            time += tomin * n
            offset = n - len(result)
            for temp in result:
                if(tomin  >= temp):break
                heapq.heappush(heap,tomin - temp)
            result.clear()
            # print(heap)
            # print(time)
        time = time - offset
        return time
        



# @lc code=end

