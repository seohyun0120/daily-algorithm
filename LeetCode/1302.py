# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return

        q = [root]
        level = []

        while q:
            for i in q:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
            
            # remain only deepest level into q
            if len(level)==0:
                break

            q = level
            level = []
            
        ans = 0

        for i in q:
            ans += i.val
        return ans