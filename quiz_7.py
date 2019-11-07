# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


placeFlag=[[1 for _ in range(dim)] for _ in range(dim)]
# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    currentColor=2
    for i in range(dim):
        for j in range(dim):
            #不为0且当前位置没有被遍历过，则是一个新的连通组
            if placeFlag[i][j]==1 and grid[i][j]!=0:
                dfs(i,j,currentColor)
                currentColor+=1
    #print()
    #display_grid()
    return currentColor-2

    # Replace pass above with your code
#深搜
def dfs(i,j,color):
    if i<0 or i>dim-1 or j<0 or j>dim-1:
        return
    if placeFlag[i][j]==0 or grid[i][j]==0:
        return
    placeFlag[i][j]=0
    grid[i][j]=color
    #往四个方向遍历
    for x in [(1,0),(0,1),(-1,0),(0,-1)]:
        dfs(i+x[0],j+x[1],color)
    pass

#对于每一个shape找尖端，遍历所有部位0，判断四周是否有3个0
def max_number_of_spikes(nb_of_shapes):
    cntList=[]
    cnt=0
    for index in range(2,nb_of_shapes+2):
        for i in range(dim):
            for j in range(dim):
                if grid[i][j]==0 or grid[i][j]!=index:
                    continue
                count=0
                for x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if i+x[0]<0 or i+x[0]>dim-1 or j+x[1]<0 or j+x[1]>dim-1:
                        count+=1#越界也算
                        continue
                    if grid[i+x[0]][j+x[1]]==0:
                        count+=1
                if count==3:
                    cnt+=1
        cntList.append(cnt)
        cnt=0
    return max(cntList)
    # Replace pass above with your code


# Possibly define other functions here    


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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
