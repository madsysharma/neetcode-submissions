class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& A = nums1;
        vector<int>& B = nums2;
        
        if(B.size() < A.size())
        {            
            swap(A, B);
        }

        int n = A.size() + B.size();
        int h = (n + 1) / 2;

        int l = 0;
        int r = A.size();
        while(l <= r)
        { 
            int idx = (l + r) / 2;
            int j = h - idx;
            int aLeft = idx > 0 ? A[idx - 1] : INT_MIN;
            int bLeft = j > 0 ? B[j - 1] : INT_MIN;
            int aRight = idx < A.size() ? A[idx] : INT_MAX;
            int bRight = j < B.size() ? B[j] : INT_MAX;

            if(aLeft <= bRight && bLeft <= aRight)
            {
                if(n % 2 != 0)
                {
                    return max(aLeft, bLeft);
                }
                else
                {
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0;
                }
            }
            else if(aLeft > bRight)
            {
                r = idx - 1;
            }
            else
            {
                l = idx + 1;
            }
        }
        return -1;
    }
};