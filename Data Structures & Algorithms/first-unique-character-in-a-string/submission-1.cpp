class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, vector<int>> tab;
        int idx = -1;
        for(int i = 0; i < s.length(); i++)
        {
            char c = s[i];
            if(tab.find(c) == tab.end())
            {
                vector<int> newVect = {i};
                tab[c] = newVect;
            }
            else
            {
                tab[c].push_back(i);
            }
        }
        for(char c: s)
        {
            if(tab[c].size() == 1)
            {
                return tab[c][0];
            }
        }
        return idx;
    }
};