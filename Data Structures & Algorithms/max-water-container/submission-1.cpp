class Solution {
public:
    int maxArea(vector<int>& heights) {
       int max = 0;
       int start = 0;
       int end = heights.size() - 1;
       while(start < end){
        if((end - start) * (min(heights[start],heights[end])) > max){
            max = (end - start) * (min(heights[start],heights[end]));
        }
        if(heights[start] < heights[end]){
            start++;
        } else if(heights[start] > heights[end]){
            end--;
        } else{
            start++;
        }
       }
       return max;
       
       }
};
