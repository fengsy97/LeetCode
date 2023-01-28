/*
 * @lc app=leetcode id=2131 lang=cpp
 *
 * [2131] Longest Palindrome by Concatenating Two Letter Words
 * gg bb cc 2
 * gg bb 0
 * gg cc gg cc cc bb   10
 * xe sc ml op po lm
 * ex xe sc cs ml ml lm lm op op po po 
 */

// @lc code=start
class Solution {
public:
    int compare(string str1,string str2){
        if(str1[0] == str2[0]){
            if(str1[1] == str2[1])return 1;
            else if(str1[1] >= str2[1]) return 2;
            else return 0;
        }
        else if (str1[0] > str2[0])return 2;
        return 0;
    }
    int longestPalindrome(vector<string>& words) {
        int map[26][26] = {};
        int result = 0;
        int x,y;
        for(int i = 0; i < words.size(); i++){
            x = words[i][0] - 'a';
            y = words[i][1] - 'a';
            // cout<<" "<<words[i]<<" "<<map[x][y]<<" "<<map[y][x]<<endl;
            
            if(map[y][x] > 0){
                result += 4;
                map[y][x] --;
                // cout << words[i]<<endl;
                
            }
            else {
                map[x][y] += 1;
            }
        }
        for(int i = 0; i < 26; i++){
            if(map[i][i] == 1){
                // cout << words[i]<<endl;
                result += 2;
                break;
            }
        }
        return result;
    }
};
// @lc code=end

