#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (48.65%)
# Likes:    8241
# Dislikes: 468
# Total Accepted:    1M
# Total Submissions: 2.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root):
    # min_depth += 1
    # min_depth += 1
    # if is leaf node, set its depth = 0 and return 1
    if(not (root.left or root.right)):
        root.val = 1
        return True
    
    
    left_depth = right_depth = 0
    bool_left = bool_right = True

    if(root.left):
        bool_left = dfs(root.left)
        left_depth = root.left.val
    if(root.right):
        bool_right = dfs(root.right)
        right_depth = root.right.val
    if(not(bool_left and bool_right)):return False
    if(left_depth - right_depth > 1 or left_depth - right_depth < -1):return False
    # print(root.val)
    root.val = max(left_depth,right_depth) + 1
    # print("changed to ",root.val)
    
    return True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not root):return True

        return dfs(root)
# @lc code=end

