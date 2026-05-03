class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        int i = 0;
        for(int j = 1; j < n; j++)
        {
            if(abs(x - arr[i]) > abs(x - arr[j]))
            {
                i = j;
            }
        }

        vector<int> result = {arr[i]};
        int l = i - 1;
        int r = i + 1;
        while(result.size() < k)
        {
            if(l >= 0 && r < n)
            {
                if(abs(x - arr[l]) <= abs(x - arr[r]))
                {
                    result.push_back(arr[l--]);
                }
                else
                {
                    result.push_back(arr[r++]);
                }
            }
            else if(l >= 0)
            {
                result.push_back(arr[l--]);
            }
            else if(r < n)
            {
                result.push_back(arr[r++]);
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
};