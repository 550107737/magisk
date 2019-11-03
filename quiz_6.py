# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111
"""
思路：https://www.cnblogs.com/fstang/archive/2013/05/19/3087746.html
"""

from random import seed, randrange
import sys

dim = 10


def get_new_grid():
    x = []
    for row in range(dim):
        x.append([])
        count = 0
        for column in range(dim):
            if grid[row][column] == 1:
                count += 1
            else:
                count = 0
            x[row].append(count)
    return x


def find_square(row, column, new_grid):
    count = 1
    val = new_grid[row][column]
    # 最少一行2个
    if val == 1:
        return 0
    for i in range(row - 1, -1, -1):
        if new_grid[i][column] >= val:
            count += 1
        else:
            break
    for i in range(row + 1, dim):
        if new_grid[i][column] >= val:
            count += 1
        else:
            break
    # 最少需要两行
    if count == 1:
        count = 0
    return val * count


def find_parallelogram_left_slash(row, column, new_grid):
    count = 1
    val = new_grid[row][column]
    # 最少一行2个
    if val == 1:
        return 0
    j = column
    # 向上寻找
    for i in range(row - 1, -1, -1):
        if j < dim - 1:
            j += 1
        else:
            break
        if new_grid[i][j] >= val:
            count += 1
        else:
            break
    j = column
    # 向下寻找
    for i in range(row + 1, dim):
        if j > 0:
            j -= 1
        else:
            break
        if new_grid[i][j] >= val:
            count += 1
        else:
            break
    if count == 1:
        count = 0
    return val * count


def find_parallelogram_right_slash(row, column, new_grid):
    count = 1
    val = new_grid[row][column]
    # 最少一行2个
    if val == 1:
        return 0
    j = column
    # 向上寻找
    for i in range(row - 1, -1, -1):
        if j > 0:
            j -= 1
        else:
            break
        if new_grid[i][j] >= val:
            count += 1
        else:
            break
    j = column
    # 向下寻找
    for i in range(row + 1, dim):
        if j < dim - 1:
            j += 1
        else:
            break
        if new_grid[i][j] >= val:
            count += 1
        else:
            break
    if count == 1:
        count = 0
    return val * count


def display_grid():
    for row in grid:
        print('   ', *row)


def size_of_largest_parallelogram():
    maxVal = 0
    new_grid = get_new_grid()
    # for i in new_grid:
    #     print(i)
    for row in range(dim):
        for column in range(dim):
            if new_grid[row][column] == 0:
                continue
            area = [find_square(row, column, new_grid), find_parallelogram_left_slash(row, column, new_grid),
                    find_parallelogram_right_slash(row, column, new_grid)]
            if max(area) > maxVal:
                maxVal = max(area)
    return maxVal
    # REPLACE PASS ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS


try:

    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                               ).split()
                         )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
        for _ in range(dim)
        ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')
