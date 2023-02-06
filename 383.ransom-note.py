#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (57.95%)
# Likes:    3613
# Dislikes: 400
# Total Accepted:    693.8K
# Total Submissions: 1.2M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list1 = [0]*26
        list2 = [0]*26
        for i in range(len(ransomNote)):
            list1[ord(ransomNote[i]) - 97] += 1
        for i in range(len(magazine)):
            list2[ord(magazine[i]) - 97] += 1   
        for i in range(len(list1)):
            # print(i,list1[i],list2[i])
            if(list1[i] > list2[i]):return False
        return True
        
# @lc code=end

