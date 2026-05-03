class Solution {
public:
    vector<int> weights;
    int tot = 0;
    Solution(vector<int>& w) {
        weights = w;
        for(int i: w)
        {
            tot += i;
        }
    }
    
    int pickIndex() {
        double num = tot * ((double) rand() / RAND_MAX);
        int currSum = 0;
        for(int i = 0; i < weights.size(); i++)
        {
            currSum += weights[i];
            if(currSum > num)
            {
                return i;
            }
        }
        return -1;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */