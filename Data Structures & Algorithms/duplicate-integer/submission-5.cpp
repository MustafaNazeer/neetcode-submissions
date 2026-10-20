class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        if(std::size(nums) == 0 || std::size(nums) == 1) return false;

        std::unordered_set<int> s{};

        for(const auto& i : nums){
            s.insert(i);
        }

        if(std::size(s) != std::size(nums)) return true;
        return false;

        
    }
};