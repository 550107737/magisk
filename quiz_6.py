# Written by *** and Eric Martin for COMP9021
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


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def size_of_largest_parallelogram():
    list1 = []
    dictionary = {}
    list_buffer = []
    result = 0
    result_buffer = 0
    j = 0
    for consecutive_num in range(2, 1 + dim):
        for row in grid:
            for i in range(dim):
                for k in range(consecutive_num):
                    if i + k <= dim - 1:
                        if row[i] == row[i + k] == 1:
                            list_buffer.append(i + k)
                        else:
                            k = 0
                            break
                    else:
                        k = 0
                        break
                if k == consecutive_num - 1:
                    list1.append(tuple(list_buffer))
                list_buffer = []
            dictionary[consecutive_num,j] = list1
            j += 1
            list1 = []
        j = 0
    list_buffer = []
    for consecutive_num in range(2, 1 + dim):
        for j in range(dim):
            for i in dictionary[consecutive_num,j]:
                for l in range(len(i)):
                        list_buffer.append(i[l]+1)
                for k in range(1+j, dim):
                    if tuple(list_buffer) in dictionary[consecutive_num,k]:
                        result_buffer += consecutive_num
                        for a in range(len(list_buffer)):
                            list_buffer[a] += 1
                    else:
                        list_buffer = []
                        break
                list_buffer = []
                if result_buffer:
                    result_buffer += consecutive_num
                if result_buffer > result:
                    result = result_buffer
                result_buffer = 0
    list_buffer = []
    for consecutive_num in range(2, 1 + dim):
        for j in range(dim):
            for i in dictionary[consecutive_num,j]:
                for l in range(len(i)):
                    list_buffer.append(i[l]-1)
                for k in range(1+j, dim):
                    if tuple(list_buffer) in dictionary[consecutive_num,k]:
                        result_buffer += consecutive_num
                        for a in range(len(list_buffer)):
                            list_buffer[a] -= 1
                    else:
                        list_buffer = []
                        break
                list_buffer = []
                if result_buffer:
                    result_buffer += consecutive_num
                if result_buffer > result:
                    result = result_buffer
                result_buffer = 0
    list_buffer = []
    for consecutive_num in range(2, 1 + dim):
        for j in range(dim):
            for i in dictionary[consecutive_num,j]:
                for l in range(len(i)):
                    list_buffer.append(i[l])
                for k in range(1+j, dim):
                    if tuple(list_buffer) in dictionary[consecutive_num,k]:
                        result_buffer += consecutive_num
                    else:
                        list_buffer = []
                        break
                list_buffer = []
                if result_buffer:
                    result_buffer += consecutive_num
                if result_buffer > result:
                    result = result_buffer
                result_buffer = 0
    return result
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
