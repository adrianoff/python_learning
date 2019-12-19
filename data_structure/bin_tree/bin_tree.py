class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.value = value


class BinTree:
    def __init__(self, root: Node):
        self.root = root


import json

with open('tree.json') as fp:
    tree_json = json.load(fp)

node = Node(value=tree_json['root']['value'])


def fill_tree(node, dict):
    node.value = dict.get('value', None)
    if dict.get('left') is not None:
        node.left = fill_tree(Node(parent=node), dict.get('left'))
    if dict.get('right') is not None:
        node.right = fill_tree(Node(parent=node), dict.get('right'))

    return node


node = fill_tree(Node(), tree_json['root'])