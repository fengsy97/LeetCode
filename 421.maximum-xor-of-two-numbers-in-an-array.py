#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (54.34%)
# Likes:    4687
# Dislikes: 352
# Total Accepted:    137.6K
# Total Submissions: 253.6K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given an integer array nums, return the maximum result of nums[i] XOR
# nums[j], where 0 <= i <= j < n.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
# 
# 
# Example 2:
# 
# 
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def insert(self,num):
        root = self.root
        for i in range(32):
            i = 31 - i
            temp = 1&(num>>i)
            if(not temp in root):
                root[temp] = {}
            root = root[temp]

    def search(self,root1,root2,level,value):
        

        if(level == 31):
            if(value > self.result):
                self.result = value
            return
        value = value << 1
        # print(value)
        # if((1 in root1 and 0 in root2) or (1 in root2 and 0 in root1)):
        #     if(self.min_level > level):self.min_level = level
        if(len(root1.keys()) == 2 and len(root2.keys()) == 2):
            self.search(root1[1],root2[0],level+1,value+1)
            self.search(root1[0],root2[1],level+1,value+1)
        elif(1 in root1 and 0 in root2):
            self.search(root1[1],root2[0],level+1,value+1)
        elif(1 in root2 and 0 in root1):
            self.search(root1[0],root2[1],level+1,value+1)
        else:
            # if(self.min_level < level):return
            if(1 in root1 and 1 in root2):
                self.search(root1[1],root2[1],level+1,value)
            if(0 in root1 and 0 in root2):
                self.search(root1[0],root2[0],level+1,value)
        return
            



            
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return 0
        self.root = {}
        for num in nums:
            self.insert(num)
        # print(self.root)
        self.result = 0
        self.min_level = 33
        # self.search(self.root,self.root,0,0)
        temp_root = self.root
        level = 0
        while(len(temp_root.keys()) == 1):
            if(0 in temp_root):
                temp_root = temp_root[0]
            else:
                temp_root = temp_root[1]
            level += 1
        # print("level = ",level)
        self.search(temp_root[0],temp_root[1],level,1)

        return self.result
        # if(nums)
        
# @lc code=end

