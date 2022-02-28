public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<int> charSet = new HashSet<int>();
        int i = 0,  j = 0, maxLength = 0;
        
        while(j < s.Length){
            if(charSet.Contains(s[j])){
                charSet.Remove(s[i]);
                i++;
            }
            else {
                charSet.Add(s[j]);
                j++;
                maxLength = Math.Max(charSet.Count, maxLength);
            }
        }
        
        return maxLength;
    }
}