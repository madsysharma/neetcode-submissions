class Solution {
public:
    int helper(vector<int>& nums, vector<int>& tab)
    {
        int n = nums.size();
        if(n == 0)
        {
            return 0;
        }
        else if(n == 1)
        {
            return nums[0];
        }
        else
        {
            int secondLast = 0;
            int last = nums[0];
            int result;

            for(int i = 1; i < n; i++)
            {
                result = max(nums[i] + secondLast, last);
                secondLast = last;
                last = result;
            }
            return result;
        }
    }

    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> tab(n+1, -1);
        vector<int> nums1(nums.begin() + 1, nums.end());
        vector<int> nums2(nums.begin(), nums.end() - 1);
        return max(nums[0], max(helper(nums1, tab), helper(nums2, tab)));
    }
};
