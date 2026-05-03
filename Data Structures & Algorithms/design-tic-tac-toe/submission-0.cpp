class TicTacToe {
public:
    vector<int> rows;
    vector<int> cols;
    int diag;
    int antiDiag;
    TicTacToe(int n) {
        rows.assign(n, 0);
        cols.assign(n, 0);
        diag = 0;
        antiDiag = 0;
    }
    
    int move(int row, int col, int player) {
        int currPlayer = (player == 1) ? 1 : -1;
        rows[row] += currPlayer;
        cols[col] += currPlayer;

        if(row == col)
        {
            diag += currPlayer;
        }
        if(col == (cols.size() - row - 1))
        {
            antiDiag += currPlayer;
        }
        int len = rows.size();
        if(abs(rows[row]) == len || abs(cols[col]) == len || abs(diag) == len || abs(antiDiag) == len)
        {
            return player;
        }
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
