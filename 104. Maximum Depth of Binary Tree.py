# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursiveDepth(self, tree: TreeNode) -> int:
        if tree is None:
            return 0

        return max(self.recursiveDepth(tree.left), self.recursiveDepth(tree.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursiveDepth(root)


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
