class Solution {
public:
    bool helper(vector<int>& nums, int idx, unordered_map<int, bool>& tab)
    {
        if(tab.find(idx) != tab.end())
        {
            return tab[idx];
        }
        else if(idx == nums.size() - 1)
        {
            tab[idx] = true;
            return tab[idx];
        }
        else if(nums[idx] == 0)
        {
            tab[idx] = false;
            return tab[idx];
        }
        else
        {
            bool res = false;
            for(int i = 1; i < nums[idx] + 1; i++)
            {
                int next_idx = idx + i;
                res = res || helper(nums, next_idx, tab);
            }
            tab[idx] = res;
            return tab[idx];
        }
    }

    bool canJump(vector<int>& nums) {
        unordered_map<int, bool> tab;
        return helper(nums, 0, tab);
    }
};
