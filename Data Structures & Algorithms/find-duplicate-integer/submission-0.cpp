class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        unordered_map<int, int> hashTable;

        for(int i : nums){
            hashTable[i]++;
        }

        for(const auto& pair : hashTable){

            if(pair.second != 1){
                return pair.first;
            }
        }
    }
};
