# Problem Link: https://leetcode.com/problems/serialize-and-deserialize-bst/
from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '#'
        res = str(root.val)
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return res + ',' + left + ',' + right

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        tokens = data.split(',')
        q = Queue()
        for token in tokens:
            q.put(token)

        return self.buildTree(q)

    def buildTree(self, tokens):
        token = tokens.get()
        if token == '#':
            return None

        root = TreeNode(int(token))
        left = self.buildTree(tokens)
        right = self.buildTree(tokens)
        root.left = left
        root.right = right

        return root
