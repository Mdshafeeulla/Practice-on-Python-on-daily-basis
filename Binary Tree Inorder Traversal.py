# As this is a Binary tree inorder traversal that follows:left root and then right nodes
# And does have the complexity of O(n) which means it needs to travel every single node.
# Definition for a binary tree node.
from typing import Optional, List
# Assuming the TreeNode class is available
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node):
            if not node:
                return

            # 1. Left
            traverse(node.left)

            # 2. Root
            res.append(node.val)

            # 3. Right
            traverse(node.right)

        traverse(root)
        return res

Tree_solution = Solution()
Tree_solution.inorderTraversal([1,2,3])