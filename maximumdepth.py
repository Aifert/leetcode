# maximum depth of binary tree (easy)
# recursive DFS (depth first search)


from collections import deque


def maxDepth(root):
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# iterative BFS (Breath first search)
# using a queue we will queue the elements in the order we see then remove it and repalce it with its children
# while keeping track of the number of items we have already found, hence the maximum depth


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level


# Iterative DFS using a stack


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 1
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])

        return level
