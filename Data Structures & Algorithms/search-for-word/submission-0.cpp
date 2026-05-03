class Solution {
public:
    int rows;
    int cols;

    bool dfs(vector<vector<char>>& board, string word, int r, int c, int idx)
    {
        if(idx == word.size())
        {
            return true;
        }
        if(r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] != word[idx] || board[r][c] == '#')
        {
            return false;
        }
        board[r][c] = '#';
        bool result = dfs(board, word, r+1, c, idx+1) ||
                      dfs(board, word, r-1, c, idx+1) ||
                      dfs(board, word, r, c+1, idx+1) ||
                      dfs(board, word, r, c-1, idx+1);
        board[r][c] = word[idx];
        return result;
    }

    bool exist(vector<vector<char>>& board, string word) {
        rows = board.size();
        cols = board[0].size();

        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(dfs(board, word, r, c, 0))
                {
                    return true;
                }
            }
        }
        return false;
    }
};
