class Solution {
public:
    std::unordered_map<int, bool> tab;

    bool dp(string& s, vector<string>& wordMap, int idx)
    {
        if(tab.find(idx) != tab.end())
        {
            return tab[idx];
        }

        for(const string& word: wordMap)
        {
            if(idx + word.length() <= s.length() && s.substr(idx, word.length()) == word)
            {
                if(dp(s, wordMap, idx + word.length()))
                {
                    tab[idx] = true;
                    return true;
                }
            }
        }
        tab[idx] = false;
        return false;
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        tab[s.length()] = true;
        return dp(s, wordDict, 0);
    }
};
