#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (42.98%)
# Likes:    5840
# Dislikes: 339
# Total Accepted:    468.9K
# Total Submissions: 1.1M
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
# 
# Implement the WordDictionary class:
# 
# 
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
# 
# 
# 
# Example:
# 
# 
# Input
# 
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# 
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 3 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.
# 
# 
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.head = {}

    def addWord(self, word: str) -> None:
        temp = self.head
        for i in range(len(word)):
            if not word[i] in temp:
                temp[word[i]] = [0,{}]
            if(i == len(word) - 1):
                temp[word[i]][0] = 1
            temp = temp[word[i]][1]
    def judge(self,word,temp):
        # print(word)
        if(not word):return True
        match = 0
        for i in range(len(word)):
            if(word[i] == "."):
                if(i == len(word) - 1):
                  for letter in temp:
                    if(temp[letter][0]):return True
                  return False
                for letter in temp:
                    if(self.judge(word[i+1:],temp[letter][1])):
                        return True
                return False
            else:
                if(word[i] in temp):
                    if(i == len(word) - 1):
                        if(temp[word[i]][0]):return True
                        else: return False
                    temp = temp[word[i]][1]
                else:
                    return False
                
                
            
    def search(self, word: str) -> bool:
        temp = self.head
        return self.judge(word,temp)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

