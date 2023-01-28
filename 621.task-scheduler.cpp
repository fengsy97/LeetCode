/*
 * @lc app=leetcode id=621 lang=cpp
 *
 * [621] Task Scheduler
 */

// @lc code=start
class Solution {
public:
    class Task {
        public:
        int nums;
        char letter;
        Task(int a, char b) :nums(a), letter(b){}
    } ;

    // bool compare(Task i1, Task i2){
    //     return (i1.nums > i2.nums);
    // }

    int leastInterval(vector<char>& tasks, int n) {
        vector<char> result;
        vector<Task> Tasklist;
        for(int i = 0; i < 26; i++){
            Task temp_task(0,'A'+i);
            Tasklist.push_back(temp_task);
        }
        for(int i = 0; i < tasks.size(); i++){
            Tasklist[tasks[i]-'A'].nums ++;
        }
        sort(Tasklist.begin(), Tasklist.end(), [](const Task& lhs, const Task& rhs) {
        return lhs.nums > rhs.nums;
        });

        while(Tasklist[0].nums > 0){
            int rank = -1;
            int size = result.size();
            // for(int i = 0; i < Tasklist.size(); i++){
            //     if(Tasklist[i].nums>0)cout<<Tasklist[i].letter<<" "<<Tasklist[i].nums<<" ";
            // }
            // cout <<endl;
            for(int i = 0; i < Tasklist.size(); i++){
                rank = i;
                for(int j = 1; j <= n&& j<=size; j ++){
                    if(Tasklist[i].letter  == result[size - j]){
                        rank = -1;
                        break;
                    }
                }
                if(rank >= 0)break;
            }
            if(rank < 0 ){
                result.push_back('+');
                continue;
            }
            if(Tasklist[rank].nums>0){
                Tasklist[rank].nums--;
                result.push_back(Tasklist[rank].letter);
            }
            else{
                result.push_back('+');
                continue;
            }
            if(rank >=0 &&rank < Tasklist.size()-1){
                int swap_pos = rank;
                int end = Tasklist.size();
                int mid = 0;
                while(swap_pos < end){
                    mid = swap_pos + (end - swap_pos)/2;
                    if(Tasklist[rank].nums < Tasklist[mid].nums){
                        swap_pos = mid + 1;
                    }
                    else end = mid;
                }
                // cout<< "rank = "<< rank << " " << Tasklist[rank].letter <<" mid =  "<<end<< " "<< Tasklist[mid].letter<<endl;
                // for(;swap_pos<Tasklist.size();swap_pos++){
                //     if(Tasklist[rank].nums >= Tasklist[swap_pos].nums)break;
                // }
                if(swap_pos>rank){
                    int temp_int = Tasklist[rank].nums;
                    char temp_char = Tasklist[rank].letter;
                    Tasklist[rank].nums = Tasklist[swap_pos-1].nums;
                    Tasklist[rank].letter = Tasklist[swap_pos-1].letter;
                    Tasklist[swap_pos-1].nums = temp_int;
                    Tasklist[swap_pos-1].letter = temp_char;
                }
            }
        }
        // for(int i = 0; i < result.size(); i++){
        //     cout<<result[i]<<" ";
        // }
        return result.size();

        
    }
};
// @lc code=end

