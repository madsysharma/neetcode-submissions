class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int maxProfit = 0;
        while(l < prices.size())
        {
            int r = l + 1;
            while(r < prices.size())
            {
                maxProfit = max(maxProfit, prices[r] - prices[l]);
                r += 1;
            }
            l += 1;
        }
        return maxProfit;
    }
};
