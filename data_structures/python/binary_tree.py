
class BinaryTree:

    class Node :

        def __init__(self, data):
            self.parent = None
            self.left = None
            self.right = None
            self.data = data

    def __init__(self):
        self.root = None

    def insert(self, v):

        if self.root == None:
            self.root = self.Node(v)
            return

        queue = [self.root]

        while len(queue):

            temp = queue[0]
            queue.pop(0)

            if temp.left == None:
                temp.left = self.Node(v)
                break
            else:
                queue.append(temp.left)

            if temp.right == None:
                temp.right = self.Node(v)
                break
            else:
                queue.append(temp.right)

    def print(self):
        self.inorder(self.root)

    def inorder(self, node):

        if node == None:
            return

        self.inorder(node.left)
        print(node.data, " ")
        self.inorder(node.right)

bt = BinaryTree()
bt.insert(10)
bt.insert(11)
bt.insert(2)
bt.insert(5)
bt.insert(9)
bt.insert(110)

bt.print()

            
