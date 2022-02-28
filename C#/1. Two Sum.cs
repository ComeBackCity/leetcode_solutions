public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int length = nums.Length;
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < length; i++){
            map[nums[i]] = i;
        }
        
        for (int i = 0; i < length; i++){
            int comp = target - nums[i];
            if (map.ContainsKey(comp) && map[comp] != i){
                return new int[]{i, map[comp]};
            }
        }
        
        return new int[]{-1, -1};
    }
}