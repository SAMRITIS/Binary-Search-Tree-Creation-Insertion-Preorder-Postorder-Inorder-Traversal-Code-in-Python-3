class tree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    def node(self, data):
        if self.data:
            if self.data>data:
                if self.left is None:
                    self.left = tree(data)
                else:
                    self.left.node(data)
            elif self.data<data:
                if self.right is None:
                    self.right = tree(data)
                else:
                    self.right.node(data)
        else:
            self.data = data

    def show1(self):
        if self.data:
            print(self.data)
            if self.left:
                self.left.show1()
            if self.right:
                self.right.show1()
        else:
            return -1
    def show2(self):
        if self.data:
            if self.left:
                self.left.show2()
            if self.right:
                self.right.show2()
            print(self.data)
        else:
            return -1
    def show3(self):
        if self.data:
            if self.left:
                self.left.show3()
            print(self.data)
            if self.right:
                self.right.show3()
        else:
            return -1
root = tree(10)
root.node(50)
root.node(30)
root.node(80)
root.node(5)
root.node(2)
root.node(7)
print("Inorder")
root.show3()
print("Postorder")
root.show2()
print("Preorder")
root.show1()