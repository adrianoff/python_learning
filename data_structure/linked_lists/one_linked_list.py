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

    def append(self, data):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(data, None)
        else:
            self.last.next_node = self.last = Node(data, None)

    def push(self, data):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(data)
        else:
            self.first = Node(data, self.first)

    def insert(self, i, data):
        if type(i) is not int or i < 0:
            raise ValueError('Invalid argument i.')

        if i > self.length:
            raise ValueError('Argument i out of range.')

        if i == 0:
            self.first = Node(data, self.first)
            self.length += 1
            return

        current = self.first
        count = 0
        while current is not None:
            if i == count:
                current.next_node = Node(data, current.next_node)
                if current.next_node.next_node is None:
                    self.last = current.next_node

                self.length += 1
                break

            current = current.next_node
            count += 1

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next_node is not None:
                current = current.next_node
                out += str(current.value) + '\n'

            return out + ']'

        return 'LinkedList []'

    def __len__(self):
        return self.length


linked_list = OneLinkedList()

linked_list.append(3)
linked_list.append(45)
linked_list.push(1)
linked_list.insert(3, 7777)

print(linked_list)
print(len(linked_list))