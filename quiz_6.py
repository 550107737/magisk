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


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def size_of_largest_parallelogram():
    L = []
    D = {}
    L_tmp = []
    size_final = 0
    size_tmp = 0
    a = 0
    for consec_num in range(2,1+len(grid)):
        for row in grid:
            for i in range(len(grid[0])):
                for j in range(consec_num):
                    if i + j <= len(grid) - 1:
                        if row[i] == row[i+j] == 1:
                            L_tmp.append(i+j)
                        else:
                            j = 0
                            break
                    else:
                        j = 0
                        break
                if j == consec_num - 1:
                    L.append(tuple(L_tmp))
                L_tmp = []
            D[consec_num,a] = L
            a = a + 1
            L = []
        a = 0
    L_tmp = []

    for consec_num in range(2,1+len(grid)):
        for a in range(len(grid)):
            for i in D[consec_num,a]:
                for l in range(len(i)):
                    L_tmp.append(i[l]+1)
                for j in range(a+1,len(grid)):
                    if tuple(L_tmp) in D[consec_num,j]:
                        size_tmp = size_tmp + consec_num
                        for k in range(len(L_tmp)):
                            L_tmp[k] = L_tmp[k] + 1
                    else:
                        L_tmp = []
                        break
                L_tmp = []
                if size_tmp:
                    size_tmp = size_tmp + consec_num
                if size_tmp > size_final:
                    size_final = size_tmp
                size_tmp = 0
    L_tmp = []

    for consec_num in range(2,1+len(grid)):
        for a in range(len(grid)):
            for i in D[consec_num,a]:
                for l in range(len(i)):
                    L_tmp.append(i[l]-1)
                for j in range(a+1,len(grid)):
                    if tuple(L_tmp) in D[consec_num,j]:
                        size_tmp = size_tmp + consec_num
                    for k in range(len(L_tmp)):
                        L_tmp[k] = L_tmp[k] - 1
                    else:
                        L_tmp = []
                        break
                L_tmp = []
                if size_tmp:
                    size_tmp = size_tmp + consec_num
                if size_tmp > size_final:
                    size_final = size_tmp
                size_tmp = 0
    L_tmp = []

    for consec_num in range(2,1+len(grid)):
        for a in range(len(grid)):
            for i in D[consec_num,a]:
                for l in range(len(i)):
                    L_tmp.append(i[l])
                for j in range(a+1,len(grid)):
                    if tuple(L_tmp) in D[consec_num,j]:
                        size_tmp = size_tmp + consec_num
                    else:
                        L_tmp = []
                        break
                L_tmp = []
                if size_tmp:
                    size_tmp = size_tmp + consec_num
                if size_tmp > size_final:
                    size_final = size_tmp
                size_tmp = 0
    return size_final
                    
    

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
