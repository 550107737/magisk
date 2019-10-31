# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys


def encode(list_of_integers):
    tmp = []
    output_str = ''
    output_num = 0
    for i in range(len(list_of_integers)):
        tmp.append(bin(list_of_integers[i])[2:])
    for i in range(len(tmp)):
        tmp[i] = ''.join([a * 2 for a in tmp[i]])
        output_str = output_str + tmp[i] + "0"
        output_num = int(output_str[:-1],2)
    return output_num
def decode(integer):
    tmp = bin(integer)[2:]
    tmp = list(tmp)
    l = len(tmp)
    index = 0
    output = ''
    output_num = 0
    while (index < l):
        try:
            if tmp[index] == tmp[index + 1]:
                output = output + tmp[index]
                index = index + 2
            elif tmp[index] == '0':
                output = output + ','
                index = index + 1
            else:
                return None
                break
        except:
           return None
    output_num = [int(x,2) for x in output.split(',')]
    return output_num
# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
