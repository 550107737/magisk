import sys
import re
#import time


def check_strict_positive_int_pattern(numStr):  # 检查严格正整数
    regex = "^[1-9]\d*$"
    return re.search(regex, numStr)


def check_roman_rule(romanRule):  # 检查罗马字典是否有重复值
    n = len(romanRule)
    i = 0
    while i != n:
        if romanRule[i] in romanRule[i + 1:]:
            if not romanRule[i] == "_":
                return False
        i += 1
    return True


# 求取字典用于计算
def get_int_dict(romanRule):
    dic = {}
    length = len(romanRule) // 2 + len(romanRule) % 2
    i = 1
    while i <= length:
        if romanRule[-1 - (i - 1) * 2] == romanRule[0]:  # 罗马字典为单数最后一个
            dic[i] = ('', romanRule[-1 - (i - 1) * 2], romanRule[-1 - (i - 1) * 2] * 2,
                      romanRule[-1 - (i - 1) * 2] * 3)
        elif romanRule[-i * 2] == romanRule[0]:  # 罗马字典为双数最后一个
            dic[i] = ('', romanRule[-1 - (i - 1) * 2], romanRule[-1 - (i - 1) * 2] * 2,
                      romanRule[-1 - (i - 1) * 2] * 3,
                      romanRule[-1 - (i - 1) * 2] + romanRule[-2 - (i - 1) * 2],
                      romanRule[-2 - (i - 1) * 2], romanRule[-2 - (i - 1) * 2] + romanRule[-1 - (i - 1) * 2],
                      romanRule[-2 - (i - 1) * 2] + romanRule[-1 - (i - 1) * 2] * 2,
                      romanRule[-2 - (i - 1) * 2] + romanRule[-1 - (i - 1) * 2] * 3)
        else:
            dic[i] = ('', romanRule[-1 - (i - 1) * 2], romanRule[-1 - (i - 1) * 2] * 2,
                      romanRule[-1 - (i - 1) * 2] * 3,
                      romanRule[-1 - (i - 1) * 2] + romanRule[-2 - (i - 1) * 2],
                      romanRule[-2 - (i - 1) * 2], romanRule[-2 - (i - 1) * 2] + romanRule[-1 - (i - 1) * 2],
                      romanRule[-2 - (i - 1) * 2] + romanRule[-1 - (i - 1) * 2] * 2,
                      romanRule[-2 - (i - 1) * 2] + romanRule[-1 - (i - 1) * 2] * 3,
                      romanRule[-1 - (i - 1) * 2] + romanRule[-3 - (i - 1) * 2])
        i += 1
    return dic


def int2roman(numStr, romanRule="MDCLXVI", limitFlag=1):  # limitFlag为切换2、3模式后不需限制4000
    if not check_roman_rule(romanRule):
        raise ValueError
    if not check_strict_positive_int_pattern(numStr):  # 用正则表达式检验输入的严格正整数
        raise ValueError
    num = int(numStr)
    if limitFlag:
        if not 0 < num < 4000:
            raise ValueError
    # dic = {
    #     'one': ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
    #     'ten': ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
    #     'hundred': ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
    #     'thousand': ('', 'M', 'MM', 'MMM')
    # }
    dic = get_int_dict(romanRule)
    roman = ""
    length = len(dic)
    for i in dic:
        if i == 1:
            roman += (dic[length + 1 - i][num // (10 ** (length - i))])
        else:
            roman += (dic[length + 1 - i][(num // (10 ** (length - i))) % 10])
    return roman


# 求取字典用于计算
def get_roman_dict(romanRule):
    dic = {}
    reversedRomanRule = romanRule[::-1]
    j = 0
    for i in reversedRomanRule:
        if j % 2 == 0:
            dic[i] = 1 * 10 ** (j // 2)
        else:
            dic[i] = 5 * 10 ** (j // 2)
        j += 1
    return dic


# 自动根据设定的romanRule求取regex
def get_roman_regex(romanRule):
    regex = "^"
    if not len(romanRule) % 2 == 0:
        regex += romanRule[0] + "{0,3}"
        i = 0
        while i < len(romanRule) // 2:
            regex += "(" + romanRule[i * 2 + 2] + romanRule[i * 2] + "|" + romanRule[i * 2 + 2] + romanRule[
                i * 2 + 1] + "|" + \
                     romanRule[i * 2 + 1] + "?" + romanRule[i * 2 + 2] + "{0,3})"
            i += 1
    else:
        i = 0
        while i < len(romanRule) // 2:
            if i == 0:
                regex += "(" + romanRule[1] + romanRule[0] + "|" + romanRule[0] + "?" + romanRule[1] + "{0,3})"
            else:
                regex += "(" + romanRule[i * 2 + 1] + romanRule[i * 2 - 1] + "|" + romanRule[i * 2 + 1] + romanRule[
                    i * 2] + "|" + \
                         romanRule[i * 2] + "?" + romanRule[i * 2 + 1] + "{0,3})"
            i += 1
    regex += "$"
    return regex


# 检查罗马字符是否符合罗马字典
def check_roman(romanStr, romanRule):
    # regex = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    regex = get_roman_regex(romanRule)
    # 用正则表达式检验输入的罗马数字格式是否正确
    return re.search(regex, romanStr)


def roman2int(roman, romanRule="MDCLXVI"):
    if not check_roman_rule(romanRule):
        raise ValueError
    if not check_roman(roman, romanRule):  # 用正则表达式检验输入的罗马数字格式是否正确
        raise ValueError
    # dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dic = get_roman_dict(romanRule)
    num = 0
    try:
        for i in range(len(roman)):
            if i == 0 or dic[roman[i]] <= dic[roman[i - 1]]:
                num += dic[roman[i]]
            else:
                num += dic[roman[i]] - 2 * dic[roman[i - 1]]
    except KeyError:
        raise ValueError
    return num


minimal = 0
minimalRomanRule = ""
# not5list = []

# 递归穷举所有排列组合，找到最小的(包含_)
def get_all_sort(strList, index, romanStr):
    global minimal, minimalRomanRule
    if index == len(strList) - 1:
        romanRule = "".join(strList).lstrip("_")
        try:
            value = roman2int(romanStr, romanRule)
        except ValueError:
            return
        if minimal == 0:
            minimal = value
            minimalRomanRule = romanRule
        else:
            if value < minimal:
                minimal = value
                minimalRomanRule = romanRule
        return
    for i in range(index, len(strList)):
        if duplicated(strList, index, i):
            continue
        temp = strList[i]
        strList[i] = strList[index]
        strList[index] = temp
        get_all_sort(strList, index + 1, romanStr)
        temp = strList[i]
        strList[i] = strList[index]
        strList[index] = temp


# 递归中查找重复排列
def duplicated(strList, index, i):
    for j in range(index, i):
        if (strList[j] == strList[i]):
            return True
    return False

'''
def all_match_trick(str):
    global minimal, minimalRomanRule
    if len(str) % 2 == 0:
        str = " " + str
    j = 1
    minimalRomanRule += str[0]
    while j < len(str):
        minimalRomanRule += str[j + 1:j - 1:-1]
        j += 2
    minimal = roman2int(str.strip(), minimalRomanRule.strip())
'''

# 指定重复元素组中获取最小可能，例如ABA求得A_B
def get_smallest(romanStr):
    global minimal, minimalRomanRule
    minimal = 0
    minimalRomanRule = ""
    dicStr1 = ""
    for q in romanStr:
        if q not in dicStr1:
            dicStr1 += q
    dicStr1 = dicStr1 + "_" * (len(romanStr) - len(dicStr1))
    get_all_sort(list(dicStr1), 0, romanStr)


"""
求出可能的排列组合，每一位都有4种，例如A=>A,BA=>BA、AB、B_A、A_B,每增加一位可能数乘4
若遇到组合则优先求取最小可能的组合(group)
组合最大间隔为2位，如ABCA可行，ABCDA一定不可行
"""


# 此函数为从后往前一位一位计算加入字典
def get_all_sort_by_one_word(dicStr, index, allDicList, group=[]):
    if 0 - index - 1 == len(dicStr):
        return allDicList
    for o in group:
        if o[0] <= len(dicStr) + index <= o[1]:
            get_smallest(dicStr[o[0]:o[1] + 1:1])
            if index == -1:
                allDicList.append(minimalRomanRule)
            else:
                pattern = []
                for x in allDicList:
                    pattern.append(minimalRomanRule + x)
                    pattern.append(x + minimalRomanRule)
                    pattern.append(x + "_" + minimalRomanRule)
                    pattern.append(minimalRomanRule + "_" + x)
                allDicList = pattern
            index = index - (o[1] - o[0]) - 1
            return get_all_sort_by_one_word(dicStr, index, allDicList, group)
    if index == -1:
        allDicList.append(dicStr[-1])
    else:
        pattern = []
        for x in allDicList:
            pattern.append(dicStr[index] + x)
            pattern.append(x + dicStr[index])
            pattern.append(x + "_" + dicStr[index])
            pattern.append(dicStr[index] + "_" + x)
        allDicList = pattern
    index -= 1
    return get_all_sort_by_one_word(dicStr, index, allDicList, group)

# 此函数为从后往前二位二位计算加入字典，若在组中则优先考虑组
def get_all_sort_by_two_word(dicStr, index, allDicList, group=[]):
    if 0 - index - 1 >= len(dicStr):
        return allDicList
    for o in group:
        if o[0] <= len(dicStr) + index <= o[1]:
            get_smallest(dicStr[o[0]:o[1] + 1:1])
            if index == -1:
                allDicList.append(minimalRomanRule)
            else:
                pattern = []
                for x in allDicList:
                    pattern.append(minimalRomanRule + x)
                    pattern.append(x + minimalRomanRule)
                    pattern.append(x + "_" + minimalRomanRule)
                    pattern.append(minimalRomanRule + "_" + x)
                allDicList = pattern
            index = index - (o[1] - o[0]) - 1
            return get_all_sort_by_two_word(dicStr, index, allDicList,group)
    if index == -1:
        get_smallest(dicStr[len(dicStr) - 2::1])
        allDicList.append(minimalRomanRule)
    elif index==0-len(dicStr):
        pattern = []
        for x in allDicList:
            pattern.append(dicStr[index] + x)
            pattern.append(x + dicStr[index])
            pattern.append(x + "_" + dicStr[index])
            pattern.append(dicStr[index] + "_" + x)
        allDicList = pattern
    else:
        pattern = []
        get_smallest(dicStr[len(dicStr) + index - 1:len(dicStr) + index + 1:1])
        for x in allDicList:
            pattern.append(minimalRomanRule + x)
            pattern.append(x + minimalRomanRule)
            pattern.append(x + "_" + minimalRomanRule)
            pattern.append(minimalRomanRule + "_" + x)
        allDicList = pattern
    if (index - 1 == 0 - len(dicStr)):
        index -= 1
    else:
        index -= 2
    return get_all_sort_by_two_word(dicStr, index, allDicList,group)


def check_more_than_3(str):
    regex = "([a-zA-Z])\\1{3,}"
    return re.search(regex, str)


instruction = input("How can I help you? ").strip()
# starttime = time.time()
regex1 = "^Please convert [^\s]+$"
regex2 = "^Please convert [^\s]+ using [^\s]+$"
regex3 = "^Please convert [^\s]+ minimally$"
try:
    if re.match(regex3, instruction):
        #valueStr = instruction.lstrip("Please convert").rstrip("minimally").strip()
        valueStr = re.sub(r"Please convert +", r"", instruction).strip()
        valueStr = re.sub(r" +minimally", r"", valueStr).strip()
        if not valueStr.isalpha():
            raise ValueError
        if check_more_than_3(valueStr):
            raise ValueError
        # dicStr = ""
        # not5list = [m.group()[0] for m in re.finditer("([a-zA-Z])\\1+", valueStr)]
        dicStr = re.sub(r"(.)\1+", r"\1", valueStr)
        # print(dicStr)
        m = re.finditer(r"(.)[^\\1]\1", dicStr)
        groups = []
        for x in m:
            a = dicStr.find(x.group())
            groups.append((a, a + 2))
        m = re.finditer(r"(.)[^\\1]{2}\1", dicStr)
        for x in m:
            a = dicStr.find(x.group())
            groups.append((a, a + 3))
        groups = sorted(groups)
        # print(groups)
        # dicStr += "_" * (len(valueStr) - len(dicStr))
        # get_all_sort(list(dicStr), 0, valueStr)# 此函数为从后往前一位一位计算加入字典
        allDicList = get_all_sort_by_one_word(dicStr, -1, [], groups)
        allDicList += get_all_sort_by_two_word(dicStr, -1, [], groups)
        minimalRomanRule = ""
        minimal = 0
        # print(allDicList)
        for x in allDicList:
            try:
                value = roman2int(valueStr, x)
            except ValueError:
                continue
            if minimal == 0:
                minimal = value
                minimalRomanRule = x
            else:
                if value < minimal:
                    minimal = value
                    minimalRomanRule = x
        if not minimal == 0:
            print("Sure! It is", minimal, "using", minimalRomanRule)
        else:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        # endtime = time.time()
        # print('Running time: %s Seconds' % (endtime - starttime))
    elif re.match(regex2, instruction):
        instruction = re.sub(r"Please convert +", r"", instruction)
        leftValueStr = instruction[0:instruction.find(" using ")].strip()
        #rightValueStr = instruction.lstrip(leftValueStr).strip().lstrip("using").strip()
        rightValueStr = re.sub("using","",re.sub(leftValueStr, r"", instruction)).strip()
        if not leftValueStr.isalnum() or not rightValueStr.isalpha():
            raise ValueError
        if leftValueStr.isdigit():
            print("Sure! It is", int2roman(leftValueStr, rightValueStr, 0))
        else:
            print("Sure! It is", roman2int(leftValueStr, rightValueStr))
    elif re.match(regex1, instruction):
        valueStr = re.sub(r"Please convert +", r"", instruction).strip()
        if not valueStr.isalnum():
            raise ValueError
        if valueStr.isdigit():
            print("Sure! It is", int2roman(valueStr))
        else:
            print("Sure! It is", roman2int(valueStr))
    else:
        print("I don't get what you want, sorry mate!")
        sys.exit()
except ValueError:
    print("Hey, ask me something that's not impossible to do!")
    sys.exit()
