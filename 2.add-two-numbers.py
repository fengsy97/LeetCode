#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (40.20%)
# Likes:    24656
# Dislikes: 4771
# Total Accepted:    3.5M
# Total Submissions: 8.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        uptonext = 0
        tail1 = l1
        head1 = l1
        if(not tail1) : return l2
        while(l1 and l2):
            l1.val += l2.val + uptonext
            if(l1.val  >= 10):
                l1.val  -= 10
                uptonext = 1
            else:
                uptonext = 0
            l1 = l1.next
            l2 = l2.next
            if(l1):tail1 = l1
        if(l2):
            tail1.next = l2
            l1 = tail1.next
            tail1 = tail1.next
        # l2 = tail1
        # print(l2.val,head1.val)
        # print(uptonext)
        while(l1):
            if(uptonext):
                # print(tail1.val)
                l1.val += uptonext
            else:
                break
            if(l1.val >= 10):
                # print(uptonext,uptonext)
                l1.val -= 10
                uptonext = 1
            else:
                uptonext = 0
            
            l1 = l1.next
            if(l1):tail1 = l1
            
        if(uptonext):
            newnode = ListNode(1)
            tail1.next = newnode
        return head1
# @lc code=end

