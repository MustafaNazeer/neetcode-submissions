class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set <int> aSet(nums.begin(), nums.end());

        if(aSet.size() == nums.size()){
            return false;
        }
        return true;
    }
};