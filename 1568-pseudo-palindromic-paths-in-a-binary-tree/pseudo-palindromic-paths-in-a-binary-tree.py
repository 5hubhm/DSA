# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, counter):
            if not node:
                return 0
            
            # Increase count of current node value
            counter[node.val] += 1
            
            # If it's a leaf node
            if not node.left and not node.right:
                # Count digits with odd occurrences
                odd_count = sum(1 for v in counter if v % 2 == 1)
                
                # Backtrack before return
                counter[node.val] -= 1
                
                return 1 if odd_count <= 1 else 0
            
            # Recurse
            left = dfs(node.left, counter)
            right = dfs(node.right, counter)
            
            # Backtrack
            counter[node.val] -= 1
            
            return left + right

        # 10 because digits are from 1 to 9
        return dfs(root, [0] * 10)
