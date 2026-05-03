class Solution {
public:
    vector<string> combos;
    void addCombos(int numOpened, int numClosed, string currSeq, int n)
    {
        if(numOpened == n && numClosed == n)
        {
            combos.push_back(currSeq);
            return;
        }
        else
        {
            if(numOpened < n)
            {
                addCombos(numOpened + 1, numClosed, currSeq + "(", n);
            }
            if(numClosed < numOpened)
            {
                addCombos(numOpened, numClosed + 1, currSeq + ")", n);
            }
        }

    }
    vector<string> generateParenthesis(int n) {
        addCombos(0, 0, "", n);
        return combos;
    }
};
