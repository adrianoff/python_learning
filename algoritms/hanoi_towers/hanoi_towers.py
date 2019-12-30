from collections import namedtuple

Disk = namedtuple('Disk', 'size')


class Stack:
    _items = []

    def push(self, disk: Disk):
        self._items.append(disk)

    def pop(self):
        disk = self._items[-1]
        del(self._items[-1])
        return disk

    def get_last(self):
        if len(self._items) > 0:
            return None
        return self._items[-1]

    def __len__(self):
        return len(self._items)


stack1 = Stack()
stack1.push(Disk(size=9))
stack1.push(Disk(size=7))
stack1.push(Disk(size=5))
stack1.push(Disk(size=3))
stack1.push(Disk(size=1))

d = stack1.pop()




