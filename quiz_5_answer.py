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
import re


def get_encode_list(str):
    regex = "(\d)\\1*"
    m = re.finditer(regex, str)
    result = []
    for x in m:
        result.append(x.group(0))
    return result


def encode(list_of_integers):
    # 获得二进制list
    str = ",".join(bin(e)[2:] for e in the_input)
    list2 = str.split(",")
    # print(list2)
    finalList2 = []
    for i in list2:
        finalList2.append(re.sub(r"(\w)", r"\1\1", i))  # 用正则，使得字符串每位翻倍 i.e."123"=>"112233"
    # 从list第二个开始，在每个最前面加入相反字符，确保分割正确
    for i in range(1, len(finalList2)):
        if finalList2[i][0] == '1':
            finalList2[i] = '0' + finalList2[i]
        else:
            finalList2[i] = '1' + finalList2[i]
    finalstr = "".join(e for e in finalList2)
    return int(finalstr, 2)

    # REPLACE pass ABOVE WITH YOUR CODE


def decode(integer):
    str = bin(the_input)[2:]
    list1 = get_encode_list(str)
    # print(list1)
    finalList = [""]
    index = 0
    flag = 1
    for i in list1:
        if len(finalList) - 1 < index:
            finalList.append("")
        if len(i) % 2 == 0:
            finalList[index] += i[::2]
            flag = 1
        # 连续单独或者最后一位单独都不行
        elif flag == 0 or list1[len(list1) - 1] == i:
            # print("错误")
            return None
        # 长度为1肯定是分隔符
        elif len(i) == 1:
            if i[-1]=='1':
                return None
            flag = 0
            index += 1
        # 长度不为1取最后一位当作分隔符
        else:
            if i[-1]=='1':
                return None
            finalList[index] += i[:len(i) - 1:2]
            flag = 0
            index += 1
    a = []
    for i in finalList:
        a.append(int(i, 2))#转10进制
    return a

    # REPLACE pass ABOVE WITH YOUR CODE


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2:])
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
