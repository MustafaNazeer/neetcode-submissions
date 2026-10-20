class Solution {
public:
    int hammingWeight(uint32_t n) {
        if (n == 0) return 0;

        int total = 0;

        for(int i = 0; i < 32; i++){
            if(n % 2) total++;
            n>>=1;
        }
        return total;
    }
};
