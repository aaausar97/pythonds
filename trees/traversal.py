from node_tree import BinaryTree

def preorder(tree: BinaryTree):
    """visit root then recursively left then recusively right"""
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)

def postorder(tree: BinaryTree):
    """recusive left then recusrive right then visit root """
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)

def inorder(tree: BinaryTree):
    """recursively left then visit root then recursively right"""
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)
