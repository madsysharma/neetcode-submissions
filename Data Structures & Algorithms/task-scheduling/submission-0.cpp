class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> ct(26, 0);
        for(char t: tasks)
        {
            ct[t - 'A'] += 1;
        }

        priority_queue<int> maxHeap;
        for(int c: ct)
        {
            if(c > 0)
            {
                maxHeap.push(c);
            }
        }

        int duration = 0;
        queue<pair<int, int>> q;

        while(!maxHeap.empty() || !q.empty())
        {
            duration += 1;
            if(maxHeap.empty())
            {
                duration = q.front().second;
            }
            else
            {
                int c = maxHeap.top() - 1;
                maxHeap.pop();
                if(c > 0)
                {
                    q.push({c, duration + n});
                }
            }

            if(!q.empty() && q.front().second == duration)
            {
                maxHeap.push(q.front().first);
                q.pop();
            }
        }
        return duration;
    }
};
