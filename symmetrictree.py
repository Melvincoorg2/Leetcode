class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(t1, t2):

            # both null
            if not t1 and not t2:
                return True

            # one null
            if not t1 or not t2:
                return False

            # values differ
            if t1.val != t2.val:
                return False

            # cross check
            return (isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))

        return isMirror(root, root)