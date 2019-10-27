import sys
import math
import itertools
from collections import defaultdict

#Arabic number to Roman number'''
def A2R(input_num):
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list = ['M','CM','D','CD','C','XC','L', 'XL','X','IX','V','IV','I']
    res_r = ''
    if input_num >= 4000:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()
    else:
        for i in range(len(num_list)):
            if input_num < num_list[i]:
                continue
            else:
                while input_num >= num_list[i]:
                    input_num = input_num - num_list[i]
                    res_r = res_r + str_list[i]
    return res_r

#Roman number to Arabic number
def R2A(input_str):
    dict_RA = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if input_str == '0':
        return 0
    else:
        res_n = 0
        for i in range(0, len(input_str)):
            if i == 0 or dict_RA[input_str[i]] <= dict_RA[input_str[i - 1]]:
                res_n = res_n + dict_RA[input_str[i]]
            else:
                res_n = res_n + dict_RA[input_str[i]] - 2 * dict_RA[input_str[i - 1]]
    if A2R(int(res_n)) != input_str:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()
    else:
        print("Sure! It is", res_n)
        sys.exit()
    return res_n

#Convert 2
def A2N(arabic, newcoor):
    newcoor = newcoor[::-1]
    roma_tmp1 = ''
    roma_tmp2 = ''
    new_coor = []
    new_coor_final = []
    if len(newcoor) % 2 == 0:
        newcoor = newcoor + '%'
    else:
        newcoor = newcoor + '%' + '%'
    num_frame = int((len(newcoor) - 1) / 2)
    for i in range(num_frame):
        newcoor_frame = newcoor[2 * i: 2 * i + 3]
        i, v, x = newcoor_frame[::]
        new_coor = [i, i + v, v, i + x]
        for i in new_coor:
            new_coor_final.append(i)
    new_coor_final_1 = new_coor_final.copy()
    for i in new_coor_final_1:
        if '%' in i:
            new_coor_final.remove(i)
    num = []
    k = 0
    for i in range(len(new_coor_final)):
        if i % 4 == 0:
            a = 1 * ((10) ** k)
            num.append(a)
        if i % 4 == 1:
            a = 4 * ((10) ** k)
            num.append(a)
        if i % 4 == 2:
            a = 5 * ((10) ** k)
            num.append(a)
        if i % 4 == 3:
            a = 9 * ((10) ** k)
            num.append(a)
            k += 1
    num_list = num[::-1]
    new_coor_list = new_coor_final[::-1]
    a = str(num_list[0])
    b = int(a[0])
    if b == 1:
        b += 3
        if len(a) > 1:
            c = len(a) - 1
            b = b * (10) ** c
    else:
        b += 4
        if len(a) > 1:
            c = len(a) - 1
            b = b * (10) ** c
    res_r = ''
    if arabic >= b:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()
    else:
        for i in range(len(num_list)):
            if arabic < num_list[i]:
                continue
            else:
                while arabic >= num_list[i]:
                    arabic -= num_list[i]
                    res_r += new_coor_list[i]
    return res_r

def R2N(roman, newcoor):
    newcoor = newcoor[::-1]
    roma_tmp1 = ''
    roma_tmp2 = ''
    new_coor = []
    new_coor_final = []
    if len(newcoor) % 2 == 0:
        newcoor = newcoor + '%'
    else:
        newcoor = newcoor + '%' + '%'
    num_frame = int((len(newcoor) - 1) / 2)
    for i in range(num_frame):
        newcoor_frame = newcoor[2 * i: 2 * i + 3]
        i, v, x = newcoor_frame[::]
        new_coor = [i, i + v, v, i + x]
        for i in new_coor:
            new_coor_final.append(i)
    new_coor_final_1 = new_coor_final.copy()
    for i in new_coor_final_1:
        if '%' in i:
            new_coor_final.remove(i)
    num = []
    k = 0
    for i in range(len(new_coor_final)):
        if i % 4 == 0:
            a = 1 * ((10) ** k)
            num.append(a)
        if i % 4 == 1:
            a = 4 * ((10) ** k)
            num.append(a)
        if i % 4 == 2:
            a = 5 * ((10) ** k)
            num.append(a)
        if i % 4 == 3:
            a = 9 * ((10) ** k)
            num.append(a)
            k += 1
    dict_RA = dict(zip(new_coor_final, num))
    if roman == '0':
        return 0
    else:
        res_n = 0
        for i in range(0, len(roman)):
            if i == 0 or dict_RA[roman[i]] <= dict_RA[roman[i - 1]]:
                if roman[i] not in newcoor:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                else:
                    res_n = res_n + dict_RA[roman[i]]
            else:
                res_n = res_n + dict_RA[roman[i]] - 2 * dict_RA[roman[i - 1]]
    # if A2N(int(res_n),newcoor) != roman:
    #     print("Hey, ask me something that's not impossible to do!")
    #     sys.exit()
    # else:
        print("Sure! It is", res_n)
        sys.exit()
    return res_n

def R2N3(input_roman,newcoor):
    newcoor = newcoor[::-1]
    roma_tmp1 = ''
    roma_tmp2 = ''
    new_coor = []
    new_coor_final = []
    if len(newcoor) % 2 == 0:
        newcoor = newcoor + '%'
    else:
        newcoor = newcoor + '%' + '%'
    num_frame = int((len(newcoor) - 1) / 2)
    for i in range(num_frame):
        newcoor_frame = newcoor[2 * i: 2 * i + 3]
        i, v, x = newcoor_frame[::]
        new_coor = [i, i + v, v, i + x]
        for i in new_coor:
            new_coor_final.append(i)
    new_coor_final_1 = new_coor_final.copy()
    for i in new_coor_final_1:
        if '%' in i:
            new_coor_final.remove(i)
    num = []
    k = 0
    for i in range(len(new_coor_final)):
        if i % 4 == 0:
            a = 1 * ((10) ** k)
            num.append(a)
        if i % 4 == 1:
            a = 4 * ((10) ** k)
            num.append(a)
        if i % 4 == 2:
            a = 5 * ((10) ** k)
            num.append(a)
        if i % 4 == 3:
            a = 9 * ((10) ** k)
            num.append(a)
            k += 1
    dict_RA = dict(zip(new_coor_final, num))
    if input_roman == '0':
        return 0
    else:
        res_n = 0
        for i in range(0, len(input_roman)):
            if i == 0 or dict_RA[input_roman[i]] <= dict_RA[input_roman[i - 1]]:
                if input_roman[i] not in newcoor:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                else:
                    res_n = res_n + dict_RA[input_roman[i]]
            else:
                res_n = res_n + dict_RA[input_roman[i]] - 2 * dict_RA[input_roman[i - 1]]
        # if A2N(int(res_n),newcoor) != input_roman:
        #     print("Hey, ask me something that's not impossible to do!")
        #     sys.exit()
        # else:
        if "%" in newcoor:
            newcoor = newcoor.replace("%"," ")
        print("Sure! It is", res_n, "using", newcoor)
        sys.exit()
    return res_n

def covert3(input_roman):
    for i in range(len(input_roman)):
        c = input_roman.count(input_roman[i])
        if c == 1:
            newcoor = input_roman
            R2N3(input_roman,newcoor)
        elif c == 2:
            if i + 1 < len(input_roman) and input_roman[i + 1] == input_roman[i]:  # AA
                continue
            elif i + 2 < len(input_roman) and input_roman[i + 2] == input_roman[i]:  # ABA
                if input_roman.count(input_roman[i + 1]) != 1:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
            elif i + 3 < len(input_roman) and input_roman[i + 3] == input_roman[i]:  # ABCA
                if input_roman.count(input_roman[i + 1]) != 1 or input_roman.count(input_roman[i + 2]) != 1:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                else:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
            else:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
        elif c == 3:
            if len(input_roman) == 3 and input_roman[0] == input_roman[1] == input_roman[2]:  # AAA
                continue
            elif len(input_roman) > 3 and i + 2 < len(input_roman) and input_roman[i + 1] == input_roman[i + 2] == input_roman[i + 3]:  # AAAB
                continue
            elif i + 3 < len(input_roman) and input_roman[i + 3] == input_roman[i + 2] == input_roman[i]:  # AABBA
                if input_roman.count(input_roman[i + 1]) != 1:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
            elif i + 3 < len(input_roman) and input_roman[i + 2] != input_roman[i + 3] != input_roman[i]:  # AABCA
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
        elif c == 4:
            if i + 4 < len(input_roman) and input_roman[i] == input_roman[i + 1] == input_roman[i + 2] == input_roman[i + 4]:
                if input_roman.count(input_roman[i + 3]) == 1:
                    continue
            elif len(input_roman) == 4 and input_roman[i] == input_roman[i + 1] == input_roman[i + 2] == input_roman[i + 3]:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            elif i + 4 >= len(input_roman):
                break
            else:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
        elif c >= 5:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()

try:
    input_word = input("How can I help you? ")
    input_word = input_word.split()
    if len(input_word) < 3:
        print("I don't get what you want, sorry mate!")
        sys.exit()
    if input_word[0] != 'Please' or input_word[1] != 'convert':
        print("I don't get what you want, sorry mate!")
        sys.exit()
    if len(input_word) == 3:
        if input_word[2].startswith('0'):
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        else:
            if input_word[2].isdigit():
                print("Sure! It is", A2R(int(input_word[2])))
                sys.exit()
            else:
                R2A(input_word[2])
                sys.exit
    if len(input_word) == 5:
        if input_word[3] != 'using':
            print("I don't get what you want, sorry mate!")
            sys.exit()
        elif input_word[2].isalpha() == input_word[4].isalpha() == True:
            if len(input_word[2]) > len(input_word[4]):
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            else:
                R2N(input_word[2],input_word[4])
                sys.exit()
        elif input_word[2].isdigit() == input_word[4].isalpha() == True:
            if input_word[2].startswith('0'):
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            else:
                print("Sure! It is", A2N(int(input_word[2]),input_word[4]))
                sys.exit
        else:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
    if len(input_word) > 5:
        print("I don't get what you want, sorry mate!")
        sys.exit()
    if len(input_word) == 4:
        if input_word[3] != 'minimally':
            print("I don't get what you want, sorry mate!")
            sys.exit()
        elif input_word[2].startswith('0'):
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        elif input_word[2].isalpha() != True:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        else:
            covert3(input_word[2])
except ValueError:
    print("I don't get what you want, sorry mate!")
    sys.exit()
