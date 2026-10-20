class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0){
            return 1;
        }
        if(n == 1){
            return x;
        }
         double result;
         result = x;
        if(n < 0){
           n = n * -1;
           for(int i = 0; i < (n - 1); i++){
            result *= x;
           }

           return 1/result;

            
        }
           for(int i = 0; i < (n - 1); i++){
            result *= x;
           }

        return result;

    }
};
