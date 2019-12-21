class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.value = value


class BinTree:
    def __init__(self, root: Node):
        self.root = root

    def fill_tree(self, node, dict):
        node.value = dict.get('value', None)
        if dict.get('left') is not None:
            node.left = self.fill_tree(Node(parent=node), dict.get('left'))
        if dict.get('right') is not None:
            node.right = self.fill_tree(Node(parent=node), dict.get('right'))

        return node

    def tree_to_dict(self, node=None):
        if node is None:
            node = self.root

        dict = {'value': node.value}

        if isinstance(node.left, Node):
            dict['left'] = self.tree_to_dict(node.left)
        if isinstance(node.right, Node):
            dict['right'] = self.tree_to_dict(node.right)

        return dict

import json

with open('tree.json') as fp:
    tree_json = json.load(fp)

root_node = Node(value=tree_json['root']['value'])
tree = BinTree(root_node)
tree.fill_tree(tree.root, tree_json['root'])

dict = tree.tree_to_dict()


pass