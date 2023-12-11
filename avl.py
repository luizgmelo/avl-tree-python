class AVL:
    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right
            self.height = 1
        
    def right_rotate(self, z):
        y = z.left
        t3 = y.right
        
        z.left = t3
        y.right = z

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        z.right = t2
        y.left = z

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(z.left), self.get_height(z.right))

        return y
        
    def insert(self, root, key):
        if root is None:
            return self.Node(key)

        if key < root.key:
            if root.left is None:
                root.left = self.Node(key)
            else:
                self.insert(root.left, key)
    
        if key > root.key:
            if root.right is None:
                root.right = self.Node(key)
            else:
                self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
            
        balance = self.get_balance(root) 

        if balance > 1 and key < root.left.key:
            # left-left case or right_rotate
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            # right-right case or left_rotate
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            # left-right case
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            # right-left case
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0 
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if root is None:
            return
        print(f'{root.key} ({self.get_balance(root)}) | ', end='')
        self.pre_order(root.left)
        self.pre_order(root.right)

avl = AVL()
root = None
root = avl.insert(root, 2)
root = avl.insert(root, 1)
root = avl.insert(root, 3)
avl.pre_order(root)
