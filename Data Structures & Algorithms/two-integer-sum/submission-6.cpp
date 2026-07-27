class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        for(int i = 0; i < nums.size(); i++)
        {
            int n = nums[i];
            int d = target - n;
            auto it = find(nums.begin(), nums.end(), d);
            if(it != nums.end())
            {
                int idx = distance(nums.begin(), it);
                if (idx == i){
                    continue;
                }
                return {min(idx, i), max(idx, i)};
        return {};
            }
        }
    }
};
