class Solution {
public:
    vector<vector<int>> perms;
    void backtrack(vector<int>& nums, vector<int>& ip)
    {
        if(ip.size() == nums.size())
        {
            perms.push_back(ip);
            return;
        }

        for(int n: nums)
        {
            if(!std::ranges::contains(ip, n))
            {
                ip.push_back(n);
                backtrack(nums, ip);
                ip.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> ip;
        backtrack(nums, ip);
        return perms;
    }
};
