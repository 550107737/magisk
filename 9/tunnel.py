import os.path
import sys
from collections import deque
file_name = input("Please enter the name of the file you want to get data from: ")
if not os.path.exists(file_name):
    print('Sorry, there is no such file.')
    sys.exit()
floor,ceil=[],[]
valid_line=0
try:
    with open(file_name) as f:
        for line in f:
            line=line.strip()
            #空行
            if len(line)==0:
                continue
            valid_line+=1
            if valid_line>2:
                raise ValueError
            tmp=[]
            for i in line.split():
                tmp.append(int(i)) #去除非数字
            if valid_line==1:
                ceil=tmp.copy()
            else:
                floor=tmp.copy()
    if len(floor)<=1 or len(floor)!=len(ceil) or any(x>=y for x,y in zip(floor,ceil)):
        raise ValueError
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()

#first
west_base=ceil[0]-0.5
all_west_base=[]
while west_base>floor[0]:
    all_west_base.append(west_base)
    west_base-=1
max_west_count=-float('inf')
for i in all_west_base:
    count=0
    index=0
    while i > floor[index] and i < ceil[index]:
        count+=1
        index+=1
        if index>=len(floor):
            break
    if count>max_west_count:
        max_west_count=count
print(f"From the west, one can into the tunnel over a distance of {max_west_count}")

#second
max_inside_distance=-float('inf')
## ceil
for i in range(len(ceil)-1):
    base=ceil[i]+0.5
    while base<ceil[i+1]:
        count = 0
        for j in range(i+1,len(ceil)):
            if base<ceil[j] and base > floor[j]:
                count+=1
            else:
                break
        if count>max_inside_distance:
            max_inside_distance=count
        base+=1
## floor
for i in range(len(floor)-1):
    base=floor[i]-0.5
    while base>floor[i+1]:
        count = 0
        for j in range(i+1,len(floor)):
            if base>floor[j] and base < ceil[j]:
                count+=1
            else:
                break
        if count>max_inside_distance:
            max_inside_distance=count
        base-=1
if max_inside_distance<max_west_count:
    max_inside_distance=max_west_count
print(f"Inside the tunnel, one can into the tunnel over a maximum distance of {max_inside_distance}")
