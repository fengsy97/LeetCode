#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (54.85%)
# Likes:    9300
# Dislikes: 281
# Total Accepted:    607.2K
# Total Submissions: 1.1M
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
# 
# 
# Example 1:
# 
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printf(self,start):
        while(start):
            print(start.val)
            start = start.next
    def mergesort(self,start):
        first = start
        if(not first):return first
        second = first.next
        if(not second):return first
        if(not second.next):
            if(second.val < first.val):
                first.next = second.next
                second.next = first
                start = second
                # print(start.val,first.val,second.val)
            return start
        # print("end!")
        pre = start
        while(second):
            pre = first
            first = first.next
            if(not second.next):
                break
            second = second.next.next
        pre.next = None
        # self.printf(start)
        start = self.mergesort(start)
        first = self.mergesort(first)
        
        second = first
        first = start
        if(first.val > second.val):
            pre = second
            second = second.next
        else:
            pre = first
            first = first.next
        start = pre

        while(first and second):
            if(first.val > second.val):
                pre.next = second
                second = second.next
            else:
                pre.next = first
                first = first.next
            pre = pre.next
        while(first or second):
            if(first):
                pre.next = first
                first = first.next
            else:
                pre.next = second
                second = second.next
            pre = pre.next
        return start
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.mergesort(head)
        return head
# @lc code=end

