#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (57.07%)
# Likes:    6766
# Dislikes: 315
# Total Accepted:    528.9K
# Total Submissions: 926.3K
# Testcase Example:  '["i","love","leetcode","i","love","coding"]\n2'
#
# Given an array of strings words and an integer k, return the k most frequent
# strings.
# 
# Return the answer sorted by the frequency from highest to lowest. Sort the
# words with the same frequency by their lexicographical order.
# 
# 
# Example 1:
# 
# 
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# Example 2:
# 
# 
# Input: words =
# ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
# 
# 
# 
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
# 
#

# @lc code=start
import heapq
# def new_cmp_lt(self,a,b):
#     if(a[0] == b[0]):return a[1]>b[1]
#     else:
#         return a[0] < b[0]
# heapq.cmp_lt=new_cmp_lt

class Solution:
    def convert(self,str):
        # temp = []
        # for char in str:
        temp = [ord(c) - 97 for c in str]
        # for i in range(len(temp),self.max):
        #     temp.append(-1)
        # print(self.max)
        while(len(temp) < self.max):
            temp.append(-1)
        res = ""
        for i in temp:
            res = res +  chr(122 -i)
        return res
    
    def convert2(self,str):
        # print(str)
        # while(str[-1] == "{"):
        #     str.pop()
        temp = [ord(c) - 97 for c in str]
        while(temp[-1] == 26):
            temp.pop()
        res = ""
        for i in temp:
            res = res +  chr(122 -i)
        return res
        
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        words.reverse()
        self.max = 0
        for word in words:
            if word in count:
                count[word] += 1    
            else:
                count[word] = 1
            self.max = max(self.max,len(word))
        result = []
        for key in count:
            if(len(result ) == k):
                # print(count[key],self.convert(key))
                num,word = heapq.heappushpop(result,(count[key],self.convert(key)))
                # if(result)
                # if(result):
                #     print(result,num,word)
                #     if(num == result[0][0]):
                #         result[0] = (num,word)
            else:
                heapq.heappush(result,(count[key],self.convert(key)))
        result.sort(key=lambda num: (num[0],num[1]),reverse=1)
        return [self.convert2(word) for num,word in result]                  
# @lc code=end

