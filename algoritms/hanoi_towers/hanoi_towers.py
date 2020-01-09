from collections import namedtuple

Disk = namedtuple('Disk', 'size')


class Stack:
    def __init__(self):
        self._items = []

    def push(self, disk: Disk):
        self._items.append(disk)

    def pop(self):
        disk = self._items[-1]
        del (self._items[-1])
        return disk

    def __len__(self):
        return len(self._items)


stack1 = Stack()
stack1.push(Disk(size=9))
stack1.push(Disk(size=7))
stack1.push(Disk(size=5))
stack1.push(Disk(size=3))
stack1.push(Disk(size=1))

stack2 = Stack()
stack3 = Stack()


def move(h: int, stack1: Stack, stack2: Stack, stack3: Stack):
    if h >= 1:
        move(h-1, stack1, stack3, stack2)
        stack2.push(stack1.pop())
        move(h-1, stack3, stack2, stack1)


move(len(stack1), stack1, stack2, stack3)