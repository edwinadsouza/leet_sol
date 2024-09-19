class Solution {
public:
    int hammingWeight(int n) {
        int freq = 0;
        while (n !=0){
            freq += n & 1;
            n >>= 1;
        }
        return freq;
        
    }
};