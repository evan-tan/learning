#include <iostream>
#include <vector>

using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        // Brute force, O(n^2)
        int size = nums.size();
        vector<int> result = {0,0};
        for (int i = 0; i < size; i++)
        {
            for (int j = i+1; j < size; j++) {
                if ((nums[i] + nums[j]) == target)
                {
                    result[0] = i;
                    result[1] = j;
                }
            }
        }
        return result;

        /*
        // Map, O(n)*2
        map<int, int> complementNums;
        for (int i = 0; i < nums.size(); i++) {
            complementNums[nums[i]] = i;
        }
        vector<int> res(2);
        for (int j = 0; j < nums.size(); j++){
            int complement = target - nums[j];
            if (complementNums[complement] && complementNums[complement] != j){
                res[0] = complementNums[complement];
                res[1] = j;
            }
        }
        return res;
        */

        /*
        // Unordered Map, O(n)
        unordered_map<int, int> compNums;
        int size = nums.size();
        vector<int> res(2);
        for (int j = 0; j < size; j++){
            int complement = target - nums[j];
            if (compNums.find(target - nums[j]) != compNums.end()){
                res[0] = compNums[target - nums[j]];
                res[1] = j;
                break;
            }else{
                compNums[nums[j]] = j;
            }
        }
        return res;
        */
    }
};