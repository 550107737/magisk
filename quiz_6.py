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

# we can divide this problem into 2 part 
# the 1st part is to find a parallelogram
# the 2nd part is to calculate the size of this parallelogram
def size_of_largest_parallelogram():
# we can divide this problem into 2 part 
# the 1st part is to find a parallelogram
# the 2nd part is to calculate the size of this parallelogram
# now we start our 2nd part 
    def calculate(matrix,idx,width):
        # we can compare the same colunmn of consecutive rows 
        # if all of them is 1 we could conclude them as 1 else 0
        # however since our matrix could be 10 columns or 19 columns
        # after i tried it made some difficulties
        # but we all get 10 rows we can exchange the row and column first to make it easier
#        new_list2=[0]*
#        for i in range(0,width):
#            if 0 in matrix[0][i] or matrix [1][i]:
#                 new_list2[i]=0
#                 return new_list2
#        print(new_list2)
        
        exchange_matrix=[[]]*width
#        exchange_matrix=[]
#        for i in range(width):
#            exchange_matrix.append([])

# during this process we can also calculate the number of 1 
        newlist=[1]*dim
        for i in range(0,10):
            
            for j in range(width):
                exchange_matrix[j].append(matrix[i][idx+j])
                if matrix[i][idx+j]==0:
                    newlist[i]=0

# now we have the final list we need to calculate the size
# the size should be the length of 1 in final list * width 
# however we may have more than 1 piece of consecutive 1s in final list
# so we can desgin a counter
#        print(newlist)        
        count=[0]
        for number in newlist:
            if int(number) == 1:
                count[-1]+=1
            if int(number) == 0 and count[-1]!=0:
                count.append(0)
#        print(count)
# Notice that we should delete the condition that we only have 1 row
        for i in range(0,len(count)):
            if count[i]=='1':
                count.pop(i)
            
#        if max(count)==1:
#            return 0
#        else:
        return max(count)*width
           
#               
#        print(newlist)
               
                
#        print(exchange_matrix)
        


    # I wanna do the 1st part firstly
    # parallelogram could be divided into 3 models the rectangle 
    
    original_matrix= grid.copy()
    
    # the 2nd model is moved left one
    # I just use the code in grid when we move the row
    # the 1st row could stay unmoved and let other row to move left row-1
    # so we still have dim rows but we would have 2*dim-1 column
    # we can move each row to right with 1 block in this way  a left parallelogram could be converted to a rectangle
    
    left_moved=[[0 for _ in range(dim*2-1)] for _ in range(dim)]
    left_moved[0][0:9]=original_matrix[0]
    left_moved[1][1:10]=original_matrix[1]
    left_moved[2][2:11]=original_matrix[2]
    left_moved[3][3:12]=original_matrix[3]
    left_moved[4][4:13]=original_matrix[4]
    left_moved[5][5:14]=original_matrix[5]
    left_moved[6][6:15]=original_matrix[6]
    left_moved[7][7:16]=original_matrix[7]
    left_moved[8][8:17]=original_matrix[8]
    left_moved[9][9:18]=original_matrix[9]
    
    # the 3rd model is moved right one
    # similar to the left one 
    right_moved=[[0 for _ in range(dim*2-1)] for _ in range(dim)]
    end=18
    for i in range(0,10):
        right_moved[i][end-9:end]=original_matrix[i]
        end=end-1
#    print(left_moved)
#    print(right_moved)

# Now we got the last step to do
# We have to consider how many new rows we have to combine
# for all conditions we should check row1 and row2 return a newlist
# then row1,row2,row3 then row1,row2,row3...row10,each return a newlist and calculate the size
# then row2 row3,row2 row3...row10, till row9,row10
# then we compare all of the size and print the largest one
        
    final_result=[]
    for idx in range(dim-1):
        for width in range(2,dim-idx+1):
           final_result.append(calculate(original_matrix,idx,width)) 
           
    for idx in range(dim*2-2):
        for width in range(2,2*dim-idx-1):
           final_result.append(calculate(left_moved,idx,width))
           
    for idx in range(dim*2-2):
        for width in range(2,2*dim-idx-1):
           final_result.append(calculate(right_moved,idx,width))
#    print(final_result)
    return max(final_result)

#    for row in original_matrix:
#        print('   ', *row) 
#    for row in left_moved:
#        print('   ', *row) 
#    for row in right_moved:
#        print('   ', *row) 
#    calculate(original_matrix,0,2)
#    
        
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
