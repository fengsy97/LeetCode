#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (45.08%)
# Likes:    5870
# Dislikes: 499
# Total Accepted:    505.6K
# Total Submissions: 1.1M
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# 
# 
# Example 2:
# 
# 
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start
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
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        count = len(wordDict)
        self.head = {}
        self.judge = {}
        for i in range(count):
            if(not self.find(wordDict[i],0)):self.insert(wordDict[i])
        # print(self.head)
        return self.find(s,1)
        # return 1
# @lc code=end

