from collections import deque, namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

card = Card('7', 'diamonds')
dq = deque([card])

card2 = Card('8', 'diamonds')
dq.appendleft(card2)
print(dq)

card3 = dq.pop()
print(dq, card3)