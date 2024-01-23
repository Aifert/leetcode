# Symmetric Tree (easy)
# doing a depth first search on each of the tree simultaneously and comparing the left to right value and right to left value
# if they are equal then the tree is mirrored


class Solution(object):
    def isSymmetric(self, root):
        def dfs(left, right):
            # base case
            if not left and not right:
                return True
            elif not left or not right:
                return False
            return (
                left.val == right.val
                and dfs(left.left, right.right)
                and dfs(left.right, right.left)
            )

        return dfs(root.left, root.right)


# above is leetcode solution
#
