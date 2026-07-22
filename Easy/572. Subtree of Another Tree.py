class Solution(object):

    def isSubtree(self, root, subRoot):

        def same(a,b):

            if not a and not b:
                return True

            if not a or not b:
                return False

            return (
                a.val == b.val and
                same(a.left,b.left) and
                same(a.right,b.right)
            )

        if not root:
            return False

        if same(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )