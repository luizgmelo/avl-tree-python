import unittest
from avl import AVL

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
        
        self.assertEqual(root.key, 23)
        

if __name__ == "__main__":
   unittest.main() 
