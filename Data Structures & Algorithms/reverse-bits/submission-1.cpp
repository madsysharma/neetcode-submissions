class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        n = (n >> 16) | (n << 16); // Swapping the 16 bit halves
        n = (((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)); // Swap bytes
        n = (((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)); // Swap nibbles
        n = (((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)); // Swap bit pairs
        n = (((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)); // Swap individual bits
        return n;
    }
};
