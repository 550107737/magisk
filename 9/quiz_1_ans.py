# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from random import seed, randrange, sample
import sys
from os import path

potential_symbols = list('~!@#$%^&*+')
try:
    for_seed, nb_of_symbols = (int(x) for x in input(
        'Enter two integers, the second one being between 1 and 10 included: '
    ).split()
                               )
    if not 1 <= nb_of_symbols < 11:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
# THE LIST OF SYMBOLS YOU WILL WORK WITH
symbols = list(sample(potential_symbols, nb_of_symbols))
# THE LIST OF NUMBERS YOU WILL WORK WITH
repetitions = list(randrange(1, 10) for _ in range(nb_of_symbols))
print('Here is the list of symbols:')
print('    ', symbols)
print('Here is the list of how many times each of them is to be displayed:')
print('    ', repetitions)
# THE SYMBOL YOU WILL WORK WITH
chosen_symbol = input('What is your favourite symbol? ')
try:
    # THE NUMBER YOU WILL WORK WITH
    gap = int(input('How big do you want the gap to be '
                    '(should be 1 or more)? '
                    )
              )
    if gap < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if chosen_symbol not in symbols:
    print("Sorry, I don't recognise that symbol.")
    sys.exit()
# THE NAME OF THE FILE YOU WILL WORK WITH
instructions_file_name = input('What is the name of the file containing '
                               'the instructions? '
                               )
if not path.exists(instructions_file_name):
    print('Sorry, there is no such file.')
    sys.exit()

# INSERT YOUR CODE BELOW

# symbols - 输出的符号列表['@', '!', '$', '~', '#', '%', '&', '+']
# repetitions - 每个符号重复几次[7, 4, 2, 8, 1, 7, 7, 1]
# gap - 输出符号间隔的横竖间隔
# chosen_symbol - 选定要输出的符号
# instructions_file_name - 最后额外输出的文件名

print("I have a drawing for you...")
print("It is made of", chosen_symbol, end="")
repeated_times = repetitions[symbols.index(chosen_symbol)]
if repeated_times == 1:
    print(", repeated once,")
else:
    print(", repeated", repeated_times, "times,")
print("placed in the four corners of a rectangle,")
print("with a gap of", gap, "both horizontally and vertically.")
print()

# 开始打印图案
print(chosen_symbol * repeated_times, " " * gap, chosen_symbol * repeated_times, sep="")
for _ in range(gap):
    print()
print(chosen_symbol * repeated_times, " " * gap, chosen_symbol * repeated_times, sep="")
print()
print("Like it?")
print("I am now going to process the instructions in the file.")
print()

#开始打印instruction文件内容
with open(instructions_file_name) as f:
    for line in f:
        line=line.replace("\n","")
        if line.startswith("#") or line.isspace() or len(line)==0 or line.startswith("All"):
            continue
        #print(line)
        line=line.replace("Draw a line of ","").replace("after ","").replace("spaces","")
        extra_line=line.split()
        print(" "*int(extra_line[2]),extra_line[1]*int(extra_line[0]),sep="")
print()
print("Ok, but not a great drawing...")