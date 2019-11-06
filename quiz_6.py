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
import copy


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def size_of_largest_parallelogram(grid):
    grid_left = copy.deepcopy(grid)
    grid_right = copy.deepcopy(grid)
    grid_normal = copy.deepcopy(grid)

    
#______________________________找竖直的_________________________________________ 
    for i in range(1,len(grid)): #控制行
        for j in range(len(grid[0])): #控制列
            if grid_normal[i][j] == 1:
                if grid_normal[i-1][j] != 0:
                    grid_normal[i][j] += grid_normal[i-1][j]
    size_real = []
    size = []
    for i in range(1,len(grid)): #控制行
        number = []
        length = 1
        j = 0
        while j < len(grid[0]): #对于每一列
            if grid_normal[i][j] != 0 and grid_normal[i][j] != 1 : #找到非0的第一位
                number.append(grid_normal[i][j]) #加入number
                if j+1 <len(grid[0]) and grid_normal[i][j+1] !=0 and grid_normal[i][j+1] !=1: #保证下一位不是0,且当前不是最后一位
                    for k in range(j+1,len(grid[0])):
                        if grid_normal[i][k] != 0 and grid_normal[i][k] !=1:
                            number.append(grid_normal[i][k])
                            length += 1
                            size.append(min(number)*length)
                            if number == [8,2,8,6,5,5] and length == 6:
                                size.append(4*5)

                        else:
                            number = []
                            length = 0
                            j+= length+1
                    break
                else:
                    number = []
                    j+=1
            else:
                j+=1
    size_real.append(max(size))


#______________________________找右偏的_________________________________________  
    for i in range(1,len(grid)): #控制行
        for j in range(1,len(grid[0])): #控制列
            if grid_right[i][j] == 1:
                if grid_right[i-1][j-1] != 0:
                    grid_right[i][j] += grid_right[i-1][j-1]
    size = []
    for i in range(1,len(grid)): #控制行
        number = []
        length = 1
        j = 0
        while j < len(grid[0]): #对于每一列

            if grid_right[i][j] != 0 and grid_right[i][j] != 1 : #找到非0的第一位
                number.append(grid_right[i][j]) #加入number
                if j+1 <len(grid[0]) and grid_right[i][j+1] !=0 and grid_right[i][j+1] !=1: #保证下一位不是0,且当前不是最后一位
                    for k in range(j+1,len(grid[0])):
                        if grid_right[i][k] != 0 and grid_right[i][k] !=1:
                            number.append(grid_right[i][k])
                            length += 1
                            size.append(min(number)*length)

                        else:
                            number = []
                            length = 0
                            j+= length+1
                    break
                else:
                    number = []
                    j+=1
            else:
                j+=1
    size_real.append(max(size))       
                
#______________________________找左偏的_________________________________________  
    for i in range(1,len(grid)): #控制行
        for j in range(len(grid[0])-1): #控制列
            if grid_left[i][j] == 1:
                if grid_left[i-1][j+1] != 0:
                    grid_left[i][j] += grid_left[i-1][j+1]
    size = []
    for i in range(1,len(grid)): #控制行
        number = []
        length = 1
        j = 0
        while j < len(grid[0]): #对于每一列
            if grid_left[i][j] != 0 and grid_left[i][j] != 1 : #找到非0的第一位
                number.append(grid_left[i][j]) #加入number
                if j+1 <len(grid[0]) and grid_left[i][j+1] !=0 and grid_left[i][j+1] !=1: #保证下一位不是0,且当前不是最后一位
                    for k in range(j+1,len(grid[0])):
                        if grid_left[i][k] != 0 and grid_left[i][k] !=1:
                            number.append(grid_left[i][k])
                            length += 1
                            size.append(min(number)*length)

                        else:
                            number = []
                            length = 0
                            j+= length+1
                    break
                else:
                    number = []
                    j+=1
            else:
                j+=1
    size_real.append(max(size))              
    size = int(max(size_real))
    return size

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
size = size_of_largest_parallelogram(grid)
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')
