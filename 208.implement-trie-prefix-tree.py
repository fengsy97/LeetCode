#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (61.44%)
# Likes:    8932
# Dislikes: 109
# Total Accepted:    734K
# Total Submissions: 1.2M
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  # '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
# 
# Implement the Trie class:
# 
# 
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# 
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
# 
# 
#

# @lc code=start

class ListNode:
    def __init__(self, val='0', next=None):
        self.val = val
        self.next = next
        self.end = False

class Trie:

    def __init__(self):
        self.root = ListNode('0',{})

    def insert(self, word: str) -> None:
        temp_node = self.root
        for i in range(len(word)):
          if word[i] in temp_node.next:
            if i < len(word) - 1:
              temp_node = temp_node.next[word[i]]
            else:
              temp_node.next[word[i]].end = True
              return None
          else:
            new_node = ListNode(word[i],{})
            temp_node.next[word[i]] = new_node
            if(i == len(word)-1):
              temp_node.next[word[i]].end = True
              return None
            temp_node = new_node



    def search(self, word: str) -> bool:
        temp_node = self.root
        for i in range(len(word)):
          if word[i] in temp_node.next:
            temp_node = temp_node.next[word[i]]
          else:
            return False
        return temp_node.end

    def startsWith(self, prefix: str) -> bool:
        temp_node = self.root
        for i in range(len(prefix)):
          if prefix[i] in temp_node.next:
            temp_node = temp_node.next[prefix[i]]
          else:
            return False
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

