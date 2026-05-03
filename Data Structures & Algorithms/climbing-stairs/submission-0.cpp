class Solution {
public:
    unordered_map<int, int> tab;
    int climbStairs(int n) {
        tab[1] = 1;
        tab[2] = 2;
        for(int i = 3; i <= n; i++)
        {
            tab[i] = tab[i-1] + tab[i-2];
        }
        return tab[n];
    }
};
