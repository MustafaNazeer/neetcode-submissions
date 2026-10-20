class Solution {
public:
    bool isAnagram(string s, string t) {
        
if(s.length() != t.length()){
    return false;
}

unordered_map<char, int> string_S_CharAndFrequency;
unordered_map<char, int> string_T_CharAndFrequency;

for(char c : s){
    string_S_CharAndFrequency[c]++;
}

for(char c : t){
    string_T_CharAndFrequency[c]++;
}

for(const auto& pair : string_S_CharAndFrequency){
    
    if(string_S_CharAndFrequency[pair.first] != string_T_CharAndFrequency[pair.first]){
return false;
    }

    }
    return true;
    }
};
