class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for(string s: strs)
        {
            vector<char> sortChars(s.begin(), s.end());
            sort(sortChars.begin(), sortChars.end());
            string key(sortChars.begin(), sortChars.end());
            if(anagrams.find(key) != anagrams.end())
            {
                anagrams[key].push_back(s);
            }
            else
            {
                anagrams[key] = {s};
            }
        }
        vector<vector<string>> results;
        for(const auto& [k, v]: anagrams)
        {
            results.push_back(v);
        }
        return results;
    }
};
