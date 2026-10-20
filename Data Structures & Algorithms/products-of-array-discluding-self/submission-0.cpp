class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        std::vector<int> v(std::size(nums), 1);

        for(std::size_t i{}; i < std::size(nums); ++i){
            for(std::size_t j{}; j < std::size(nums); ++j){

                if(i == j) continue;

                if(nums[j] == 0){
                    v[i] = 0;
                    break;
                }

                v[i] *= nums[j];
            }
        }
        return v;

    }
};
