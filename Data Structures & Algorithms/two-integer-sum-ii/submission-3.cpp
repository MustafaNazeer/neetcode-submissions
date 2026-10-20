class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
// numbers sorted in order = {1,2,3,4..}


int* start = &numbers[0]; // index 1
int* end = &numbers[numbers.size() - 1]; // index 2

while(*start < *end){

if(*start + *end == target){
    return {(int)(start - numbers.data()) + 1, (int)(end - numbers.data()) + 1};
}

if(*start + *end > target){
    end--;
}

if(*start + *end < target){
    start++;
}

}

    }
};
