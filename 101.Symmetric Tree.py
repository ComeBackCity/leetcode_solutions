# Problem Link: https://leetcode.com/problems/symmetric-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursiveCheck(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        if tree1 is None and tree2 is None:
            return True
        elif tree1 is None or tree2 is None:
            return False

        return (tree1.val == tree2.val) and self.recursiveCheck(tree1.left, tree2.right) and self.recursiveCheck(tree1.right, tree2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.recursiveCheck(root, root)


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(3)
    t2.left = t4
    t3.left = t5
    t1.left = t2
    t1.right = t3
    print(solution.isSymmetric(t1))
