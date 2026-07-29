class Solution {
public:
    bool helper(vector<int>& nums, int idx)
    {
        if(idx == nums.size() - 1)
        {
            return true;
        }
        else if(nums[idx] == 0)
        {
            return false;
        }
        else
        {
            bool res = false;
            for(int i = 1; i < nums[idx] + 1; i++)
            {
                int next_idx = idx + i;
                res = res || helper(nums, next_idx);
            }
            return res;
        }
    }

    bool canJump(vector<int>& nums) {
        return helper(nums, 0);
    }
};
