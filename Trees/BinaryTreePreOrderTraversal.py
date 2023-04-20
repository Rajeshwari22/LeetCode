class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Base case
        if root is None:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
