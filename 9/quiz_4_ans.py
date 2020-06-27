# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Generates a list L of random positive integers, at least one
# of which is strictly positive, and prints out:
# - a list "fractions" of strings of the form 'a/b' such that:
#   . a <= b,
#   . a*n and b*n both occur in L for some n, and
#   . a/b is in reduced form
# enumerated from smallest fraction to largest fraction
#  (0 and 1 are exceptions, being represented as such rather than as
# 0/1 and 1/1);
# - if "fractions" contains 1/2, then the fact that 1/2 belongs to "fractions";
# - otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
#  if that member is unique;
# - otherwise, the two members "closest_1" and "closest_2" of "fractions" that
# are closest to 1/2, in their natural order.


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = (int(x) for x in
                      input('Enter three nonnegative integers: ').split()
                                      )
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

# INSERT YOUR CODE HERE
def cal_fratcions(str2):
    if not '/' in str2:
        return int(str2)
    fenzi,fenmu=str2.split("/")
    return int(fenzi)/int(fenmu)

# 计算列表
if 0 in L:
    fractions.append('0')
fractions.append('1')

from itertools import combinations
for fenmu,fenzi in combinations(sorted(L,reverse=True),2):
    div=gcd(fenzi,fenmu)
    fenzi//=div
    fenmu//=div
    str1=f"{fenzi}/{fenmu}"
    if str1 not in fractions and '0' not in str1 and str1!='1/1':
        fractions.append(str1)

fractions=sorted(fractions,key=cal_fratcions)
# 计算cloest
if '1/2' in fractions:
    spot_on=True
else:
    fractions2=fractions.copy()
    fractions2.append('1/2')
    fractions2=sorted(fractions2,key=cal_fratcions)
    index=fractions2.index('1/2')
    if index==0:
        closest_1=fractions2[1]
    elif fractions2[index]==fractions2[-1]:
        closest_1=fractions2[-2]
    else:
        left, right= cal_fratcions(fractions2[index-1]),cal_fratcions(fractions2[index+1])
        if abs(left-0.5)==abs(right-0.5):
            closest_1,closest_2=fractions2[index-1],fractions2[index+1]
        else:
            closest_1=fractions2[index-1] if abs(left-0.5)<abs(right-0.5) else fractions2[index+1]

print('\nThe fractions no greater than 1 that can be built from L, '
      'from smallest to largest, are:'
     )
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
