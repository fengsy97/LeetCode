#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (36.00%)
# Likes:    7317
# Dislikes: 1345
# Total Accepted:    693.7K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list = []
        if(not head):return head
        while(head):
            list.append(head)
            head = head.next
        tail = list[-1]
        head = list[0]
        k %= len(list)
        for i in  range(k):
            head = list.pop()
        if(list):
            list[-1].next = None
        if(k):tail.next = list[0]
        return head


# @lc code=end

