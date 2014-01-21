# intersection test code

# colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)	

# others
num_rows = 10
num_columns = 5
board_colours = []

# make colour board - blue
for i in range(num_rows):
    board_colours.append([BLUE] * num_columns)
orig_bc = board_colours

# generate some blocks to overwrite
pieces = [[1, 2], [3, 3], [9, 4]]

# check for overlap - long way
free = []
for i, j in enumerate(board_colours):
    for k, l in enumerate(j):
        board_colours[i][k] = BLACK
        for m in pieces:
            if m[0] == i and m[1] == k:
                board_colours[i][k] = (9, 9, 9)
            else:
                pass

        



# print stuff
print "Original array: ", orig_bc
print "========================================================"
print "Original pieces: ", pieces
print "========================================================"
print "New array: ", board_colours
