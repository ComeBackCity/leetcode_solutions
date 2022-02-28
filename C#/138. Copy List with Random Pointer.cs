/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node CopyRandomList(Node head) {
        if (head == null){
            return head;
        }
        
        Dictionary<Node, Node> nodeMap = new Dictionary<Node, Node>();
        
        var temp = head;
        
        while(temp != null){
            nodeMap[temp] = new Node(temp.val);
            temp = temp.next;
        }
        
        temp = head;
        
        while(temp != null){
            if (temp.next != null){
                nodeMap[temp].next = nodeMap[temp.next];
            }
            temp = temp.next;
        }
        
        temp = head;
        
        while(temp != null){
            if(temp.random != null){
                nodeMap[temp].random = nodeMap[temp.random];
            }
            temp = temp.next;
        }
        
        return nodeMap[head];
    }
}