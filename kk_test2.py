# Find Maximum Depth of Binart Tree

from extratypes import Tree  # library with types used in the task
T = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def solution(T):
        # write your code in Python 3.6
        if T.l == None and T.r == None:
            # Has no subtree
            return 0
        elif T.l == None:
            # Only has right subtree
            return 1 + solution(T.r)
        elif T.r == None:
            # Only has left subtree
            return 1 + solution(T.l)
        else:
            # Have two subtrees
            return 1 + max(solution(T.l), solution(T.r))
