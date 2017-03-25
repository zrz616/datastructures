class BinarySelect(object):
    """docstring for BinarySelect"""
    def __init__(self, ordered_list):
        self.ordered_list = ordered_list
        self.left = 0
        self.right = len(self.ordered_list) - 1

    # 通过递归查找
    def recursion_select(self, value):
        if self.left < self.right:
            self.mid = (self.right + self.left) // 2
            if self.ordered_list[self.mid] < value:
                self.left = self.mid
            elif self.ordered_list[self.mid] > value:
                self.right = self.mid
            else:
                return self.mid
            return self.recursion_select(value)
        return -1

    # 通过循环查找
    def unrecursion_select(self, value):
        while self.left <= self.right:
            self.mid = (self.right + self.left) // 2
            if self.ordered_list[self.mid] < value:
                self.left = self.mid
            elif self.ordered_list[self.mid] > value:
                self.right = self.mid
            else:
                return self.mid
        return -1
