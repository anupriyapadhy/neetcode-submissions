# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.dfs(root,result)
        return result
        
    def dfs(self,node,result):
        if not node:
            return 
        
        self.dfs(node.left, result)
        self.dfs(node.right, result)
        result.append(node.val)