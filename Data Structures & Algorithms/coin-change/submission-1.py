class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        tab = [float('inf')] * (amount + 1)
        tab[0] = 0

        for i in range(n):
            for j in range(1, amount + 1):
                if (j - coins[i]) >= 0:
                    tab[j] = min(tab[j], 1 + tab[j - coins[i]])
        
        return tab[amount] if tab[amount] != float('inf') else -1