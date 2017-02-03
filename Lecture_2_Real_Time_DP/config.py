# A grid of 20 x 20
# O: cell is blocked (reward = 0)
# -: cell is not blocked (reward != 0)
grid = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'S', 'O', 'O', '-', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'E', 'O', 'O', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'O', 'O', 'O', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

allactions = ('E', 'N', 'W', 'S')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
discount = 1.0
iteration = 100
