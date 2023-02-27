#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (65.82%)
# Likes:    7074
# Dislikes: 260
# Total Accepted:    939.5K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane and an integer k, return the k closest points to the origin (0,
# 0).
# 
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
# 
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in).
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
# 
# 
#



# @lc code=start
class Solution:
    def dis(self,vector):
        return vector[0] * vector[0] + vector[1] * vector[1]
    def insert(self,heap,target):
        heap.append(target)
        start = len(heap) - 1
        while(int((start - 1)/2) >= 0 and self.dis(heap[int((start - 1)/2)]) > self.dis(heap[start]) ):
            target = heap[int((start - 1)/2)]
            heap[int((start - 1)/2)] = heap[start]
            heap[start] = target
            start = int((start - 1)/2)
    def shift(self,heap):
        start = 0
        while(2 * start + 1 < len(heap)):
            target = 0
            if(2 * start + 2 < len(heap)):
                if(self.dis(heap[2 * start + 2]) > self.dis(heap[2 * start + 1])):
                    if(self.dis(heap[start]) > self.dis(heap[2 * start + 1])):
                        target = 2 * start + 1
                else :
                    if(self.dis(heap[start]) > self.dis(heap[2 * start + 2])):
                        target = 2 * start + 2
            else:
                if(self.dis(heap[start]) > self.dis(heap[2 * start + 1])):
                    target = 2 * start + 1
            if(target):
                # print(start,target)
                heap[start].append(heap[target].pop(0))
                heap[start].append(heap[target].pop(0))
                heap[target].append(heap[start].pop(0))
                heap[target].append(heap[start].pop(0))
                start = target
            else:break
        return
    def pop(self,heap):
            temp = heap[0]
            heap[0] = heap[-1]
            heap[-1] = temp
            # print(heap)
            self.shift(heap[:-1])
            # print(heap)
            return heap.pop()

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for vector in points:
            self.insert(heap,vector)
        # print(heap)
        result = []
        for i in range(k):
            result.append(self.pop(heap))
            # print(heap)
        # return heap
        return result
        
        
# @lc code=end

