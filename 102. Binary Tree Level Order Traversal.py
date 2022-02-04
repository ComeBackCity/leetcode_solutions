# Problem Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
from typing import Optional, List
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time = O(n) memory = O(1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = queue.Queue()
        q.put(root)

        while not q.empty():
            level = []
            q_len = q.qsize()

            for _ in range(q_len):
                if n := q.get():
                    level.append(n.val)
                    q.put(n.left)
                    q.put(n.right)

            if level:
                res.append(level)

        return res
