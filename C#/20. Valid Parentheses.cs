public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> parenthesis_map = new Dictionary<char, char>(){
            {')','('},
            {'}','{'},
            {']','['}
        };
        
        Stack<char> myStack = new Stack<char>();
        
        foreach(char c in s){
            if (c =='(' || c == '{' || c == '['){
                myStack.Push(c);
            }
            else{
                if (myStack.Count == 0 || parenthesis_map[c] != myStack.Pop()){
                    return false;
                }
            }
        }
        
        if (myStack.Count != 0){
            return false;
        }
        
        return true;
    }
    
}