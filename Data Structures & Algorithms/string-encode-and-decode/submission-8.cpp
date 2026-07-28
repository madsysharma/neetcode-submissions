class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for(const string& s: strs)
        {
            res += to_string(s.size());
            res += "#";
            res += s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int idx = 0;
        while(idx < s.size())
        {
            int ptr = idx;
            while(s[ptr] != '#')
            {
                ptr += 1;
            }
            int l = stoi(s.substr(idx, ptr-idx));
            idx = ptr + 1;
            ptr = idx + l;
            res.push_back(s.substr(idx, l));
            idx = ptr;
        }
        return res;
    }
};
