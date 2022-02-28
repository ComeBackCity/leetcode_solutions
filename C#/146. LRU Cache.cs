public class Node {
    public int key, val;
    public Node prev, next;
    
    public Node(int key, int val, Node prev=null, Node next=null){
        this.key = key;
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}

public class LRUCache {
    public Dictionary<int, Node> cache = new Dictionary<int, Node>();
    int cap;
    Node head, tail;
    
    public LRUCache(int capacity) {
        cap = capacity;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public void Add(Node n){
        var prv = tail.prev;
        prv.next = n;
        n.next = tail;
        tail.prev = n;
        n.prev = prv;
    }
    
    public void Remove(Node n){
        var prv = n.prev;
        var nxt = n.next;
        prv.next = nxt;
        nxt.prev = prv;
    }
    
    public int Get(int key) {
        if (cache.ContainsKey(key)){
            Remove(cache[key]);
            Add(cache[key]);
            return cache[key].val;
        }
        
        return -1;
    }
    
    public void Put(int key, int value) {
        if (cache.ContainsKey(key)){
            Remove(cache[key]);
        }
        cache[key] = new Node(key, value);
        Add(cache[key]);
        
        if (cache.Count > cap){
            var lru = head.next;
            Remove(lru);
            cache.Remove(lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */