class Node(object):
    """docstring for Node"""
    def __init__(self, data, parent_node):
        self.left = None
        self.right = None
        self.heigh = 0
        self.data = data
        self.parent_node = parent_node

    def insert(self, data):
        if data <= self.data:
            if not self.left:
                self.left = Node(data, self)
                self.heigh = max(self.heigh, 1)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data, self)
            else:
                self.right.insert(data)

    # 左子树的左子树比右子树高
    def left_left_rotate(self):
        p = self.left
        self.left, p.right = p.right, self
        p.parent_node, self.parent_node = self.parent_node, p

    # 右子树的右子树比左子树高
    def right_right_rotate(self):
        p = self.right
        self.right, p.left = p.left, self
        p.parent_node, self.parent_node = self.parent_node, p

    # 左子树的右子树比右子树高
    def left_right_rotate(self):
        self.left.right_right_rotate()
        self.left_left_rotate()

    # 右子树的左子树比左子树高
    def right_left_rotate(self):
        self.right.left_left_rotate()
        self.right_right_rotate()
