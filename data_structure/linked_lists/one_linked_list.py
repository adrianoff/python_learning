
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class OneLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def clear(self):
        self.__init__()

