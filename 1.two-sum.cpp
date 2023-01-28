/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result,nums_copy;
        for(int i = 0; i < nums.size(); i++){
            nums_copy.push_back(nums[i]);
        }
        std::sort(nums.begin(), nums.end());
        
        int left,right;
        left = 0;
        right = nums.size()-1;
        while(1){
            if(nums[left] + nums[right] > target){
                right--;
            }
            else if(nums[left] + nums[right] == target){
                break;
            }
            else{
                left ++;
                if(right < nums.size()-1)right++;
            }
            // cout<<left<<" fsy "<<right<<endl;
        }
        // cout<<nums[left]<<" fsy "<<nums[right]<<endl;
        for(int i = 0; i < nums.size(); i++){
            // cout<<"nums_copy"<<i<<" " <<nums_copy[i]<<endl;
            if(nums_copy[i] == nums[left]){
                left = i;
                break;
            }
            // if(nums_copy[nums.size()-1-i] == nums[right])right = nums.size()-1-i;
        }
        for(int i = nums.size()-1; i >= 0; i--){
            if(nums_copy[i] == nums[right]){
                right = i;
                break;
            }
            // if(nums_copy[nums.size()-1-i] == nums[right])right = nums.size()-1-i;
        }
        
        result.push_back(left);
        result.push_back(right);
        return result;

    }
};
// @lc code=end

