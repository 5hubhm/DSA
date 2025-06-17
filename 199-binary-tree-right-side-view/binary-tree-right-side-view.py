# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root, lvl):
            if not root:
                return 
            if lvl == len(ans):
                ans.append(root.val)
            traverse(root.right, lvl+1)
            traverse(root.left, lvl+1)
        ans = []
        traverse(root, 0)
        return ans