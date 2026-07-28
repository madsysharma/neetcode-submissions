class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for(int n: nums)
        {
            if(counts.find(n) != counts.end())
            {
                counts[n] += 1;
            }
            else
            {
                counts[n] = 1;
            }
        }

        vector<tuple<int, int>> elems;
        for(const auto& [k,v]: counts)
        {
            tuple<int, int> e = {v, k};
            elems.push_back(e);
        }
        
        priority_queue<tuple<int, int>> maxHeap;
        for(const auto& e: elems)
        {
            maxHeap.push(e);
        }
        vector<int> results;
        int ct = 0;
        while(!maxHeap.empty() && ct != k)
        {
            auto [v, k] = maxHeap.top();
            results.push_back(k);
            ct += 1;
            maxHeap.pop();
        }
        return results;
    }
};
