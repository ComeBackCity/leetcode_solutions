public class Solution {
    public int MaxArea(int[] height) {
        int l = 0, r = height.Length - 1;
        int maxArea = Math.Min(height[l], height[r]) * (r-l);
        while(l < r){
            if(height[l] < height[r]){
                l++;
            }
            else {
                r--;
            }
            
            int area = Math.Min(height[l], height[r]) * (r-l);
            maxArea = Math.Max(maxArea, area);
        }
        
        return maxArea;
    }
}