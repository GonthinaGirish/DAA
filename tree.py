class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item
def PreOrder(root):
    if root:
        print(f"{root.item} ->", end=" ")
        PreOrder(root.left)
        PreOrder(root.right)
def InOrder(root):
    if root:
        InOrder(root.left)
        print(f"{root.item} ->", end=" ")
        InOrder(root.right)
def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(f"{root.item} ->", end=" ")
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.left.left = Node("H")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")
print('Preorder:', end=' ')
PreOrder(root)
print('\nInorder:', end=' ')
InOrder(root)
print('\nPostorder:', end=' ')
PostOrder(root)
