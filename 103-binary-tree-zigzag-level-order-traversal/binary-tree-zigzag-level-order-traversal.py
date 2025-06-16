# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        left_right = True

        while queue:
            level_len = len(queue)
            level_nodes = []
            for i in range(level_len):
                ele = queue.popleft()
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                level_nodes.append(ele.val)
            if left_right:
                ans.append(level_nodes)
            else:
                ans.append(level_nodes[::-1])
            left_right = not left_right
        return ans

                


        