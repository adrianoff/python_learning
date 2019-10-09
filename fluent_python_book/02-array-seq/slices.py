l = [10, 20, 30, 40, 50]
print(l[:2], l[2:])

print(l[::2])

s = slice(None, None, 2)
print(l[s])


l = list(range(10))
print(l)
print(l[2:5])
l[2:5] = [20, 30]
print(l)


print([1, 2] * 5)
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'O'
print(weird_board)