#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (73.13%)
# Likes:    16586
# Dislikes: 283
# Total Accepted:    2.9M
# Total Submissions: 3.9M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
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
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):return head
        temp_pre = None
        temp_next = head.next
        while(temp_next):
            head.next = temp_pre
            temp_pre = head
            head = temp_next
            temp_next = temp_next.next
        head.next = temp_pre
        return head
# @lc code=end

