class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0){
            return 1;
        }
        if(n == 1){
            return x;
        }

        if(n < 0){
           double result = x;
           n = n * -1;
           for(int i = 0; i < (n - 1); i++){
            result *= x;
           }

           return 1/result;

            
        }
        double result = x;
           for(int i = 0; i < (n - 1); i++){
            result *= x;
           }

        return result;

    }
};
