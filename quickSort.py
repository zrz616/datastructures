from random import randint


class QuickSort(object):
    """docstring for QuickSort"""

    def __init__(self, raw_list):
        self.sorted_list = raw_list[:]
        self.length = len(raw_list)
        self._quick_sort(0, len(raw_list) - 1)

    def _partition(self, left, right):
        """
        :parm left: 待partition序列的第一个元素索引
        :parm right: 待partition序列的末尾元素索引
        """
        pivot = self.sorted_list[left]

        j = left
        for i in range(left + 1, right + 1):
            if self.sorted_list[i] < pivot:
                j += 1
                self.sorted_list[j], self.sorted_list[i] = \
                    self.sorted_list[i], self.sorted_list[j]
        self.sorted_list[left], self.sorted_list[j] = \
            self.sorted_list[j], self.sorted_list[left]
        return j

    def _quick_sort(self, left, right):
        if left < right:
            pivot = self._partition(left, right)
            self._quick_sort(left, pivot - 1)
            self._quick_sort(pivot + 1, right)

    def __call__(self):
        return self.sorted_list

    # 辅助测试函数
    def test_helper(self):
        for i in range(1, self.length):
            assert self.sorted_list[i - 1] <= self.sorted_list[i]
        print('OK!')


class RandomQuickSort(QuickSort):
    """对近乎有序的序列优化"""
    def _partition(self, left, right):
        # 随机取pivot
        rand_index = randint(left, right)  # 随机取[left...right]
        self.sorted_list[rand_index], self.sorted_list[left] = \
            self.sorted_list[left], self.sorted_list[rand_index]
        return super()._partition(left, right)


class UnrecursionQuickSort(QuickSort):
    """
        通过循环迭代实现非递归快速排序，
        用栈存储划分的边界，栈为空时跳出循环
    """
    def _quick_sort(self, left, right):
        index_stack = []
        while True:
            pivot = self._partition(left, right)
            print(pivot, left, right)
            if left < pivot - 1:
                index_stack.extend([left, pivot - 1])
            if pivot + 1 < right:
                index_stack.extend([pivot + 1, right])
            if not index_stack:
                break
            right = index_stack.pop()
            left = index_stack.pop()


class ThreeWaysQuickSort(QuickSort):
    """
        对大量重复元素的情况优化
    """
    def _partition(self, raw_header, raw_tail):
        """
        :param raw_header: 未处理序列的头索引，初始时为待partition序列的第一个元素索引
        :param raw_tail: 未处理序列的尾索引，初始时为待partition序列的尾索引
        """
        rand_index = randint(raw_header, raw_tail)
        self.sorted_list[rand_index], self.sorted_list[raw_header] = \
            self.sorted_list[raw_header], self.sorted_list[rand_index]
        pivot, pivot_index = self.sorted_list[raw_header], raw_header
        less_index = pivot_index  # 小于pivot序列的尾索引
        raw_header += 1  # 第一个元素选为pivot
        while raw_header <= raw_tail:
            if self.sorted_list[raw_header] == pivot:
                raw_header += 1
            elif self.sorted_list[raw_header] < pivot:
                less_index += 1
                self.sorted_list[less_index], self.sorted_list[raw_header] = \
                    self.sorted_list[raw_header], self.sorted_list[less_index]
                raw_header += 1
            else:
                self.sorted_list[raw_tail], self.sorted_list[raw_header] = \
                    self.sorted_list[raw_header], self.sorted_list[raw_tail]
                raw_tail -= 1
        self.sorted_list[pivot_index], self.sorted_list[less_index] = \
            self.sorted_list[less_index], self.sorted_list[pivot_index]
        # 若不存在小于pivot的元素，则less_index是传入raw_header - 1
        less_index -= 1
        great_index = raw_tail + 1

        return less_index, great_index

    def _quick_sort(self, left, right):
        # 这个判断可以解决前一次partition时，
        # 小于pivot或大于pivot的元素不存在的情况
        if left < right:
            less_index, great_index = self._partition(left, right)
            self._quick_sort(left, less_index)
            self._quick_sort(great_index, right)
