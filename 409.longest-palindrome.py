#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (54.45%)
# Likes:    4326
# Dislikes: 261
# Total Accepted:    466.2K
# Total Submissions: 856.9K
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
# 
# 
# Example 1:
# 
# 
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose
# length is 7.
# 
# 
# Example 2:
# 
# 
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is
# 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count =  [0]*52
        # print(count)
        for i in range(len(s)):
            if ord(s[i])>96:
                count[ord(s[i]) - 97] += 1
            else:
                count[26+ord(s[i]) - 65] += 1
        length = 0
        odd = 0
        for nums in count:
            if(nums%2):odd = 1
            length += (nums>>1)<<1
        return length + odd


# @lc code=end

