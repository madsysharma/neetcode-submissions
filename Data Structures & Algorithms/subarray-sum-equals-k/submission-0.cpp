class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> tab;
        int tot = 0;
        int currSum = 0;
        tab[0] = 1;

        for(int n: nums)
        {
            currSum += n;
            int rem = currSum - k;
            tot += tab[rem];
            tab[currSum] += 1;
        }

        return tot;
    }
};