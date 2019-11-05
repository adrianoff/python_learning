from collections import abc, namedtuple
import random

Card = namedtuple('Card', ['rank', 'suit'])


class Deck(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __setitem__(self, index, value):
        self._cards[index] = value

    def __delitem__(self, index):
        del self._cards[index]

    def insert(self, index, value):
        self._cards.insert(index, value)

    def __getitem__(self, index):
        return self._cards[index]

    def __len__(self):
        return len(self._cards)


a = Deck()
a.append(Card(2, 'diamonds'))
random.shuffle(a)
print(a.pop())
