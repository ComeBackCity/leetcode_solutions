# Problem Link: https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time = O(mn) memory = O(1)
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t: return True
        if not s: return False
        if self.same(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def same(self, t1, t2):
        if not t1 or not t2:
            return t1 == t2

        if t1.val == t2.val:
            return self.same(t1.left, t2.left) and self.same(t1.right, t2.right)


class Solution2:
    # time = O(m+n) memory = O(m+n)
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def treeToStr(n):
            if not n:
                return ",#"

            return "," + str(n.val) + treeToStr(n.left) + treeToStr(n.right)

        ss = treeToStr(s)
        ts = treeToStr(t)

        return ts in ss
