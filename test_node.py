class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# nums = [4,5,1,9]
node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node1.next = node2
node2.next = node3


print(node1.val)
print(node1.next.next.val)
print(node2.val)
print(node3.val)
