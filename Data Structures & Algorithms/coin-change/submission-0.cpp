class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        const int INF = amount + 1;

        vector<int> dp(amount + 1, INF);
        dp[0] = 0;

        for (int j = 1; j <= amount; ++j) {
            for (int coin : coins) {
                if (coin <= j) {
                    dp[j] = min(dp[j], 1 + dp[j - coin]);
                }
            }
        }

        return dp[amount] == INF ? -1 : dp[amount];
    }
};