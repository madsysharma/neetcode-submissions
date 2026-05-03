class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n, -1);
        vector<int> right(n, n);
        stack<int> stack;

        for(int i = 0; i < n; i++)
        {
            while(!stack.empty() && heights[stack.top()] >= heights[i])
            {
                stack.pop();
            }
            if(!stack.empty())
            {
                left[i] = stack.top();
            }
            stack.push(i);
        }
        while(!stack.empty())
        {
            stack.pop();
        }
        for(int i = n - 1; i >= 0; i--)
        {
            while(!stack.empty() && heights[stack.top()] >= heights[i])
            {
                stack.pop();
            }
            if(!stack.empty())
            {
                right[i] = stack.top();
            }
            stack.push(i);
        }
        int maxArea = 0;
        for(int i = 0; i < n; i++)
        {
            left[i] += 1;
            right[i] -= 1;
            maxArea = max(maxArea, heights[i] * (right[i] - left[i] + 1));
        }

        return maxArea;
    }
};
