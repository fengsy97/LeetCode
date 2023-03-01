#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (45.54%)
# Likes:    13501
# Dislikes: 569
# Total Accepted:    1.3M
# Total Submissions: 2.8M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start

# class ListNode:
#     def __init__(self, val='', next=None):
#         self.val = val
#         self.end = 0
#         self.next = next
class Solution:
    def insert(self,word):
        temp = self.head
        for i in range(len(word)):
            if not word[i] in temp:
                temp[word[i]] = [0,{}]
            if(i == len(word) - 1):
                temp[word[i]][0] = 1
            temp = temp[word[i]][1]
        # temp[0]
    def find(self,s,judge):
        # print(s)

        temp = self.head
        # print(judge)
        if(not s):
            return True
        if(judge and s in self.judge):
            return self.judge[s]
        for i in range(len(s)):
            if(s[i] in temp):
                if(temp[s[i]][0]):
                    if(self.find(s[i+1:],judge)):
                        if(judge):self.judge[s] = True
                        return True
                temp = temp[s[i]][1]
            else:
                if(judge):self.judge[s] = False
                return False

        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        count = len(wordDict)
        self.head = {}
        self.judge = {}
        for i in range(count):
            if(not self.find(wordDict[i],0)):self.insert(wordDict[i])
        # print(self.head)
        return self.find(s,1)
        # return 1
# @lc code=end

