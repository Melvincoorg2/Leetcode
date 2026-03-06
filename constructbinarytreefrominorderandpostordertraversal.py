def buildTree(self, inorder, postorder):

        # map value -> index in inorder
        inorder_index = {v: i for i, v in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            # root value
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # split inorder
            idx = inorder_index[root_val]

            # build right subtree first
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)