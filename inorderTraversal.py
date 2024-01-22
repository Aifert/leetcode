# In order traversal (easy)
# In order means traversing the left subtree first before processing the root then going to the right subtree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    res = []

    def inorder(root):
        # if there is nothing in the root return nothing
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
        res.append(root.val)

    return res


# above is the leetcode solution
# Solution illustrates a situation where if there is nothing in the left node then it will go to the right node and repeat the same thing

# Iterative solution
