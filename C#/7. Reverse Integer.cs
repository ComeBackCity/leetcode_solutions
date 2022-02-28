public class Solution {
    public int Reverse(int x) {
        bool isNeg = x < 0;
        if (isNeg){
            x *= -1;
        }
        long res = 0;
        
        while(x > 0){
            int y = x%10;
            x /= 10;
            res = res * 10 + y;
        }
        
        if(isNeg){
            res = -res;
        }
        
        if(res < Int32.MinValue || res > Int32.MaxValue){
            res = 0;
        }
        
        return (int)res;
    }
}