class Solution {
public:
    int maxArea(vector<int>& heights) {
        
        // two pointers start from left and right 
        int left = 0; 
        int right = heights.size() - 1; 

        int maxArea = min(heights[left], heights[right]) * (right - left);  

        while (left < right){
            if(heights[left] < heights[right]){
                left++; 
            } else {
                right--; 
            }

            int area = min(heights[left], heights[right]) * (right - left);

            if(area > maxArea){
                maxArea = area; 
            }
        }

        return maxArea; 



    }
};
