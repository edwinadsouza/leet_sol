class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /* sorted array
        vector<int> ans;
        int n = nums.size();

        int i = 0;
        int j = n-1;

        while(i<j){
            int ps = nums[i]+nums[j];
            if (ps>target){
                j--;
            } else if (ps<target){
                i++;
            } else {
                ans.push_back(i);
                ans.push_back(j);
                return ans;

            }

        }
        return ans;
        */
        // unsorted array
        unordered_map<int, int> numMap; // value -> index
        vector<int> ans;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numMap.find(complement) != numMap.end()) {
                ans.push_back(numMap[complement]);
                ans.push_back(i);
                return ans;
            }
            numMap[nums[i]] = i;
        }
        return ans;


        
    }
    
};