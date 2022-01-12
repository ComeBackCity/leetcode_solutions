# Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        list_length = len(nums)
        if list_length == 0:
            return None
        mid = list_length // 2
        root = TreeNode(nums[mid])
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid + 1:len(nums)])
        root.left = left
        root.right = right

        return root


if __name__ == '__main__':
    solution = Solution()
    tree = solution.sortedArrayToBST([-11, 0, 1, 4, 6])
