class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_set<int> aSet{};

        for(const auto& i : nums){
            aSet.insert(i);
        }

        if(std::size(aSet) != std::size(nums)) return true; return false;

    }
};