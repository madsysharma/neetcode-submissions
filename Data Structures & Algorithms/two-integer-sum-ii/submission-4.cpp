class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i = 0; i < numbers.size(); i++)
        {
            int l = i+1;
            int r = numbers.size() - 1;
            int temp = target - numbers[i];

            while(l <= r)
            {
                int m = l + ((r - l) / 2);
                if(numbers[m] == temp)
                {
                    return {i+1, m+1};
                }
                else if(numbers[m] < temp)
                {
                    l = m + 1;
                }
                else
                {
                    r = m - 1;
                }
            }
        }
        return {};
    }
};
