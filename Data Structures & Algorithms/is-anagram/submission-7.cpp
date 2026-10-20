class Solution {
public:
    bool isAnagram(string s, string t) {

        if(std::size(s) != std::size(t)) return false;
        
        std::unordered_map <char, int> hash1{};
        std::unordered_map <char, int> hash2{};

        for(const auto& c : s){
            hash1[c]++;
        }

        for(const auto& c : t){
            hash2[c]++;
        }

        
        return hash1 == hash2;

    }
};
