class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int fresh = 0;
        int duration = 0;

        for(int r = 0; r < grid.size(); r++)
        {
            for(int c = 0; c < grid[0].size(); c++)
            {
                if(grid[r][c] == 1)
                {
                    fresh += 1;
                }
                if(grid[r][c] == 2)
                {
                    q.push({r,c});
                }
            }
        }

        vector<pair<int, int>> dirs = {{0,1}, {0, -1}, {1, 0}, {-1, 0}};
        while(fresh > 0 && !q.empty())
        {
            int n = q.size();
            for(int i = 0; i < n; i++)
            {
                auto curr = q.front();
                q.pop();
                int r = curr.first;
                int c = curr.second;

                for(const auto& d: dirs)
                {
                    int row = r + d.first;
                    int col = c + d.second;
                    if(row >=0 && row < grid.size() && col >= 0 && col < grid[0].size() && grid[row][col] == 1)
                    {
                        grid[row][col] = 2;
                        q.push({row, col});
                        fresh -= 1;
                    }
                }
            }
            duration += 1;
        }
        if(fresh == 0)
        {
            return duration;
        }
        else
        {
            return -1;
        }
    }
};
