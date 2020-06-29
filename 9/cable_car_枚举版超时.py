import os.path
import sys

from collections import defaultdict
file_name = input("Please enter the name of the file you want to get data from: ")
if not os.path.exists(file_name):
    print('Sorry, there is no such file.')
    sys.exit()

cable=[]
try:
    with open(file_name) as f:
        for line in f:
            line=line.strip()
            #空行
            if len(line)==0:
                continue
            for i in line.split():
                cable.append(int(i)) #去除非数字
    if min(cable)<=0 or len(cable)<=1 or len(cable)!=len(set(cable)) or cable!=sorted(cable):
        raise ValueError
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()

slope=[]
for i in range(len(cable)-1):
    slope.append(cable[i+1]-cable[i])

# 寻找连续出现最多次的斜率
longest_good_ride_times=1
cur_good_ride_times=1
for i in range(1,len(slope)):
    if slope[i]==slope[i-1]:
        cur_good_ride_times+=1
    else:
        cur_good_ride_times=1
    if cur_good_ride_times>longest_good_ride_times:
        longest_good_ride_times=cur_good_ride_times
if longest_good_ride_times==len(slope):
    print("The ride is perfect!")
else:
    print("The ride could be better...")

print(f"The longest good ride has a length of: {longest_good_ride_times}")
from itertools import combinations
min_remove=-float('inf')
for i in range(2,len(cable)+1):
    for j in combinations(cable,i):
        if i!=2:
            diff=j[1]-j[0]
            flag=0
            for k in range(2,len(j)):
                if j[k]-j[k-1]!=diff:
                    flag=1
                    break
            if flag:
                continue
        remove=len(cable)-len(j)
        if remove<min_remove:
            min_remove=remove

print(f"The minimal number of pillars to remove to build a perfect ride from the rest is: {min_remove}")
