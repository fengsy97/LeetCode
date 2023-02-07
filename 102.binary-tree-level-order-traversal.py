#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (63.90%)
# Likes:    12264
# Dislikes: 242
# Total Accepted:    1.7M
# Total Submissions: 2.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
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
def mid_find(root,result,depth):
    if(not root):return
    if(len(result) <= depth):
        result.append([root.val])
    else:
        # print(len(result),depth)
        result[depth].append(root.val)
    mid_find(root.left,result,depth+1)
    mid_find(root.right,result,depth+1)
    return
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result  = []
        mid_find(root,result,0)
        return result
# @lc code=end

