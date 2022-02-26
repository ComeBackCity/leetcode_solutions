# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursiveTraversal(self, root: TreeNode, order: List[int]) -> List[int]:
        if root.left is not None:
            self.recursiveTraversal(root.left, order)
        order.append(root.val)
        if root.right is not None:
            self.recursiveTraversal(root.right, order)

        return order

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.recursiveTraversal(root, []) if root is not None else []


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t2.left = t3
    t1.right = t2
    print(solution.inorderTraversal(None))
