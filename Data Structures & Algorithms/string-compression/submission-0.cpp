class Solution {
public:
    int compress(vector<char>& chars) {
        int len = chars.size();
        int i = 0;
        int j = 0;

        while(i < len)
        {
            chars[j++] = chars[i];
            int k = i + 1;
            while(k < len && chars[i] == chars[k])
            {
                k++;
            }
            if(k - i > 1)
            {
                string count = to_string(k - i);
                for(char c : count)
                {
                    chars[j++] = c;
                }
            }
            i = k;
        }
        return j;
    }
};