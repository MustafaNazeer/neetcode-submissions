class Solution {
public:
    bool isAnagram(string s, string t) {

        if(std::size(s) != std::size(t)) return false;
        
        std::sort(std::begin(s), std::end(s));
        std::sort(std::begin(t),std::end(t));

        if(s != t) return false;
        return true;

    }
};
