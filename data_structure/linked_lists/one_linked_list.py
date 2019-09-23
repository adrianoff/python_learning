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

    def insert(self, position, data):
        if type(position) is not int or position < 0:
            raise ValueError('Invalid argument i.')

        if position > self.length:
            raise ValueError('Argument i out of range.')

        if position == 0:
            self.first = Node(data, self.first)
            self.length += 1
            return

        current = self.first
        count = 0
        while current is not None:
            if position == count+1:
                current.next_node = Node(data, current.next_node)
                if current.next_node.next_node is None:
                    self.last = current.next_node

                self.length += 1
                break

            current = current.next_node
            count += 1

    def delete(self, position):
        if type(position) is not int or position < 0:
            raise ValueError('Invalid argument i.')

        if position > self.length:
            raise ValueError('Argument i out of range.')

        if position == 0:
            if self.first.next_node is not None:
                self.first = self.first.next_node
            else:
                self.first = self.last = None

            self.length -= 1
            return

        current = self.first
        count = 0
        while current is not None:
            if position == count + 1:
                if current.next_node.next_node is not None:
                    current.next_node = current.next_node.next_node
                    self.length -= 1
                else:
                    current.next_node = None
                    self.last = current
                    self.length -= 1
                break

            current = current.next_node
            count += 1

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

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
linked_list.insert(1, 7777)
print(linked_list)
linked_list.delete(0)

print(linked_list)
print(len(linked_list))
print(linked_list.get_first().value)
print(linked_list.get_last().value)
