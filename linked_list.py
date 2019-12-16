""" 連結リスト的な """


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


class LinkedList:
    """ 単方向リスト """
    def __init__(self, root=None):
        self.first = root
        self.last = None
        self._all = []  # 生成要素の確認用

    def append_to_tail(self, data):
        """ appendメソッド(書籍コードの再現) """
        if not self.first:
            self.first = Node(data)
            self._all.append(self.first)
            return
        n = self.first
        while n.next is not None:
            n = n.next
        n.next = Node(data)
        self.last = n.next
        self._all.append(n.next)

    @property
    def all_nodes(self):
        return [n.data for n in self._all]


#  ver.1
# class LinkedList:
#     """ 単方向リスト """
#     first = None
#     last = None
#     all_ = []  # 生成要素の確認用
#
#     def __init__(self, data=None, next_=None):
#         self.data = data
#         self.next = next_
#         LinkedList.all_.append(self)
#
#         if LinkedList.first is None:
#             LinkedList.first = self
#
#     def append_to_tail(self, data):
#         """ appendメソッド(書籍コードの再現) """
#         n = self
#         while n.next is not None:
#             n = n.next
#         n.next = LinkedList(data)
#         LinkedList.last = n.next
#
#     @classmethod
#     def show_all(cls):
#         n = LinkedList.first
#         print(n.data)
#         i = 1
#         while n.next is not None:
#             n = n.next
#             print(n.data)
