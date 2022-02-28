public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int i = 0, minLength = int.MaxValue, total = 0;
        
        for(int j=0; j<nums.Length; j++){
            total += nums[j];
            while(total >= target){
                minLength = Math.Min(minLength, j-i+1);
                total -= nums[i++];
            }
        }
        
        return (minLength == int.MaxValue) ? 0: minLength;
    }
}