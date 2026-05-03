class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currMax = nums[0];
        int maxHere = nums[0];

        for(int i = 1; i < nums.size(); i++)
        {
            maxHere = max(nums[i], maxHere + nums[i]);
            currMax = max(currMax, maxHere);
        }
        return currMax;
    }
};
