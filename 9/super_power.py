import sys
try:
    heroes = [int(x) for x in input("Please input the heroes' powers: ").strip().split()]
    # if not len(heroes):
    #     raise ValueError
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
try:
    nb_of_swiches = int(input('Please input the number of power flips: ').strip())
    if nb_of_swiches<0 or nb_of_swiches>len(heroes):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
#first
sorted_heroes=sorted(heroes)
if nb_of_swiches%2==0:
    minus1=list(range(0,nb_of_swiches+1,2))
else:
    minus1 = list(range(1, nb_of_swiches + 1, 2))
# minus1=[]
# nb_of_swiches_copy=nb_of_swiches
# while nb_of_swiches>=0:
#     minus1.append(nb_of_swiches)
#     nb_of_swiches_copy-=2
max_sum=-float('inf')
for i in minus1:
    ret=sorted_heroes.copy()
    index=0
    while i>0:
        ret[index]*=-1
        i-=1
        index+=1
    if sum(ret)>max_sum:
        max_sum=sum(ret)
print(f"Possibly flipping the power of the same hero many times, the greatest achievable power is {max_sum}.")

#second
max_sum=-float('inf')

ret=sorted_heroes.copy()
index=0
i=nb_of_swiches
while i>0:
    ret[index]*=-1
    i-=1
    index+=1
if sum(ret)>max_sum:
    max_sum=sum(ret)
print(f"Flipping the power of the same hero at most once, the greatest achievable power is {max_sum}.")

#third
minus1=[-1]*nb_of_swiches+[1]*(len(heroes)-nb_of_swiches)
all_minus1=[]
all_minus1.append(minus1.copy())
while -1 in minus1 and minus1[-1]!=-1:
    minus1=[minus1.pop()]+minus1
    all_minus1.append(minus1.copy())
all_heroes=[]
for j in all_minus1:
    all_heroes.append([x*y for x,y in zip(j,heroes)])
max_sum=-float('inf')
for i in all_heroes:
    if sum(i)>max_sum:
        max_sum=sum(i)
print(f"Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {max_sum}.")

# forth
all_minus1=[]
for i in range(len(heroes)+1):
    minus1=[-1]*i+[1]*(len(heroes)-i)
    all_minus1.append(minus1.copy())
    while -1 in minus1 and minus1[-1]!=-1:
        minus1=[minus1.pop()]+minus1
        all_minus1.append(minus1.copy())
all_heroes=[]
for j in all_minus1:
    all_heroes.append([x*y for x,y in zip(j,heroes)])
max_sum=-float('inf')
for i in all_heroes:
    ret=sum(i)
    if ret>max_sum:
        max_sum=ret
print(f"Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {max_sum}.")


    

