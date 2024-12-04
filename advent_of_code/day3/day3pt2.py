import re

file_path = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day3/raw.txt'
with open(file_path, 'r') as file:
    raw_text = file.read()

regex_toggle = r"(don't\(\)|do\(\))"
regex_mul = 'mul\([0-9]{1,3},[0-9]{1,3}\)'
split_regex = r'[(,)]'

parts = re.split(regex_toggle, raw_text)

def clean_mul(string_input: str) -> int:
    clean1 = re.split(split_regex, string_input)
    int_1, int_2 = int(clean1[1]), int(clean1[2])
    return int_1 * int_2

def toggle_mul(txt) -> list:
    on = True
    muls = []
    for item in txt:
        print(item)
        if item == "don't()":
            on = False
        elif item == "do()":
            on = True
        elif re.search(regex_mul, item) and on:
            lst = re.findall(regex_mul, item)
            print(lst)
            mullist = [clean_mul(i) for i in lst]
            print(mullist)
            muls.extend(mullist)
            print(muls)
    return muls

final = toggle_mul(parts)
print(sum(final))