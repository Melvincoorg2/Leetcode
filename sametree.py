class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Case 1: both are None
        if not p and not q:
            return True

        # Case 2: one is None
        if not p or not q:
            return False

        # Case 3: values differ
        if p.val != q.val:
            return False

        # Recursive check left and right
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))