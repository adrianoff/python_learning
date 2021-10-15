from time import time
import random


class Tree:
    def __init__(self):
        self.l = None
        self.r = None
        self.p = None
        self.v = None


def insert_tree(v: int, tree: Tree):
    if tree.v is None:
        tree.v = v
    else:
        if tree.v < v:
            if tree.l is not None:
                insert_tree(v, tree.l)
            else:
                nt = Tree()
                nt.v = v
                nt.p = tree
                tree.l = nt
        else:
            if tree.r is not None:
                insert_tree(v, tree.r)
            else:
                nt = Tree()
                nt.v = v
                nt.p = tree
                tree.r = nt


def print_tree(tree, h=0):
    if tree is not None and tree.v is not None:
        print_tree(tree.l, h + 1)
        print(' ' * 4 * h + '->', tree.v)
        print_tree(tree.r, h + 1)


if __name__ == '__main__':
    tree = Tree()
    N = 10
    els = [random.randint(0, 100) for i in range(N)]
    [insert_tree(el, tree) for el in els]
    print(els)
    print_tree(tree)

    pass
