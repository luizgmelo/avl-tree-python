import unittest
from avl import AVL, Node

class TestAVLMethods(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()

    def test_insert(self):
        tree = self.avl
        root = None
        root = tree.insert(root, 10)
        root = tree.insert(root, 23)
        root = tree.insert(root, 52)
        root = tree.insert(root, 33)
        root = tree.insert(root, 44)
        root = tree.insert(root, 15)
        """
                23
            10      44
              15  33  52

        """
        self.assertEqual(root.key, 23)
        self.assertEqual(root.right.key, 44)
        self.assertEqual(root.left.key, 10)

    def test_rotate_left(self):
        root = Node(3)
        rightChild = Node(6)
        root.right = rightChild
        leftGrandChild = Node(5)
        rightGrandChild = Node(7)
        rightChild.left = leftGrandChild
        rightChild.right = rightGrandChild

        tree = self.avl
        rotated = tree.left_rotate(root)
        self.assertEqual(rotated.key, 6)
        self.assertEqual(rotated.left.key, 3)
        self.assertEqual(rotated.right.key, 7)
        self.assertEqual(rotated.left.right.key, 5)
        
    def test_rotate_right(self):
        root = Node(8)
        leftChild = Node(6)
        root.left = leftChild
        leftGrandChild = Node(5)
        rightGrandChild = Node(7)
        leftChild.left = leftGrandChild
        leftChild.right = rightGrandChild

        tree = self.avl
        rotated = tree.right_rotate(root)
        self.assertEqual(rotated.key, 6)
        self.assertEqual(rotated.left.key, 5)
        self.assertEqual(rotated.right.key, 8)
        self.assertEqual(rotated.right.left.key, 7)
        

if __name__ == "__main__":
   unittest.main() 
