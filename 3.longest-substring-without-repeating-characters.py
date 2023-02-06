#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.81%)
# Likes:    31911
# Dislikes: 1399
# Total Accepted:    4.2M
# Total Submissions: 12.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        temp_length = 0
        hashtable = {}
        if(not s): return 0
        hashtable[s[0]] = 0
        temp_length = 1
        max_length = 1
        for i in range(1,len(s)):
            if(s[i] in hashtable):
                end = hashtable[s[i]]+1
                start = i - temp_length
                for j in range(start,end):
                    del hashtable[s[j]]
                hashtable[s[i]] = i
                temp_length = len(hashtable)
            else:
                hashtable[s[i]] = i
                temp_length += 1
                max_length = max(temp_length,max_length)
        return max_length
# @lc code=end

