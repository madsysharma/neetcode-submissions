class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int l = nums.size();
        vector<int> res(l, 1);

        for(int i = 1; i < l; i++)
        {
            res[i] = res[i-1] * nums[i-1];
        }

        int postFix = 1;
        for(int j = l-1; j >= 0; j--)
        {
            res[j] *= postFix;
            postFix *= nums[j];
        }

        return res;
    }
};
