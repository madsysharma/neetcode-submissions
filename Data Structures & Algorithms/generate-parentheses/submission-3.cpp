class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<vector<string>> tab(n+1);
        tab[0] = {""};

        for(int i = 0; i <= n; i++)
        {
            for(int j = 0; j < i; j++)
            {
                for(const string& left: tab[j])
                {
                    for(const string& right: tab[i-j-1])
                    {
                        tab[i].push_back("(" + left + ")" + right);
                    }
                }
            }
        }

        return tab[n];
    }
};
