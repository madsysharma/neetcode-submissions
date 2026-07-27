class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length())
        {
            return false;
        }
        else
        {
            std::unordered_map<char, int> cmapS;
            std::unordered_map<char, int> cmapT;
            for(int i = 0; i < s.length(); i++)
            {
                cmapS[s[i]] += 1;
                cmapT[t[i]] += 1;
            }
            if(cmapS == cmapT)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
};
