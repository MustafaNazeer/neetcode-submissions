class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        if(std::size(nums) == 0) return {};
        if(std::size(nums) == 1 && nums[0] != target) return {};

        std::unordered_map<int,int> hash{};

        for(std::size_t i{}; i < std::size(nums); ++i){
            hash[nums[i]] = i;
        }

        for(int i{}; i < std::size(nums); ++i){

            int val{target - nums[i]};

            if(hash.find(val) != hash.end() && hash[val] != i){
                return {std::min(hash[val], i), std::max(hash[val],i)};
            }
        }
        return {};



    }
};
