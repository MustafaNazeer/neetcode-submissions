#include <algorithm>

class Solution {
public:
    bool isPalindrome(string s) {

transform(s.begin(), s.end(), s.begin(), ::toupper);

char* start = &s[0];
char* end = &s[s.length() - 1];

while(start < end){
    if(!isalnum(*start)){
        start++;
        continue;
    } else if(!isalnum(*end)){
        end--;
        continue;
    }

 if(*start != *end){
    return false;
    }

    start++;
    end--;
}
return true;
    }
};