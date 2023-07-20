class Node:
    # Node class for the Binary Search Tree
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    # Binary Search Tree class
    def __init__(self):
        self.root = None

    def insert(self, key):
        # Insert a key into the BST
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # Helper function to recursively insert a key into the BST
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def inorder_traversal(self):
        # Perform an inorder traversal of the BST
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        # Helper function for inorder traversal
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

def main():
    # Challenge: Implement a BST and perform operations on it
    bst = BinarySearchTree()

    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)

    print("Inorder Traversal of BST:")
    print(bst.inorder_traversal())

if __name__ == "__main__":
    main()
