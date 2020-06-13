# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from random import seed, randrange, sample
import sys
from os import path


try: 
    for_seed, upper_bound, size =\
         (int(x) for x in input('Enter three nonnegative integers: ').split())
    if for_seed < 0 or upper_bound < 0 or size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
w = len(str(upper_bound - 1))
with open('mapping.txt', 'w') as mapping:
    for (a, b) in zip(sorted(randrange(upper_bound) for _ in range(size)),
                      (randrange(upper_bound) for _ in range(size))
                     ):
        print(f'{a:{w}}', '->', b, file=mapping)                
print('Here is the mapping that has been generated:')
with open('mapping.txt') as mapping:
    for line in mapping:
        print(line, end='')

valid_mapping = True
most_frequent_inputs = []
function = {}

# INSERT YOUR CODE HERE

ret={}
with open('mapping.txt') as mapping:
    for line in mapping:
        line=line.strip()
        values=[int(x) for x in line.split(" -> ")]
        if values[0] in ret.keys():
            ret[values[0]].append(values[1])
        else:
            ret[values[0]]=[values[1]]
max=0
for v in ret.values():
    if len(set(v))!=len(v):
        valid_mapping=False
        break
    if len(v)>max:
        max=len(v)
if valid_mapping:
    for k,v in ret.items():
        if len(v)==max:
            most_frequent_inputs.append(k)
        if len(v)==1:
            function[k]=v[0]

if not valid_mapping:
    print("Sorry, that's not a correct mapping.")
else:
    print("Ok, that's a correct mapping.")
    print('The list of most frequent inputs is:\n\t', most_frequent_inputs)
    print('The function extracted from the mapping is:\n\t', function)
