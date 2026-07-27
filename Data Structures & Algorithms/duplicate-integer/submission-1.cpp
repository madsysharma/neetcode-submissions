class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int n: nums)
        {
            if(seen.find(n) != seen.end())
            {
                return true;
            }
            seen.insert(n);
        }
        return false;
    }
};