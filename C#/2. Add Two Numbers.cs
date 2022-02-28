/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        else if(l2 == null){
            return l1;
        }
        
        int len1 = 0, len2 = 0, carry = 0;
        ListNode temp1 = l1, temp2 = l2, large, small, toReturn;
        
        while(temp1 != null){
            len1++;
            temp1 = temp1.next;
        }
        
        while(temp2 != null){
            len2++;
            temp2 = temp2.next;
        }
        
        if(len1 >= len2){
            large = l1;
            small = l2;
        }
        else {
            large = l2;
            small = l1;
        }
        
        toReturn = large;
        
        while(true){
            int sum = carry;
            carry = 0;
            
            if (large != null){
                sum += large.val;
            }
            
            if (small != null){
                sum += small.val;
                small = small.next;
            }
            
            if (sum >= 10){
                sum -= 10;
                carry = 1;
            }
            
            large.val = sum;
            if (large.next == null && carry == 1){
                large.next = new ListNode(carry);
                break;
            }
            
            if (large != null){
                large = large.next;
            }
            
        }
        
        return toReturn;
    }
}