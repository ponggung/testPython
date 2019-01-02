import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # DFS
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # BFS
    def maxDepth_(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = collections.deque([root])
        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


T = [3, 9, 20, None, None, 15, 7]
queue = collections.deque(T)
node = queue.popleft()
queue.append(node)
print(queue)

# tree = TreeNode(0)
# tree.left = TreeNode(9)
# tree.right = TreeNode(20)
# tree.left.left = TreeNode(None)
# tree.left.right = TreeNode(None)
# tree.right.left = TreeNode(15)
# tree.right.right = TreeNode(7)

# foo = Solution()
# n = foo.maxDepth(T)
# print(n)