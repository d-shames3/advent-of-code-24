import re

file_path = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day3/raw.txt'
with open(file_path, 'r') as file:
    raw_text = file.read()

regex = 'mul\([0-9]{1,3},[0-9]{1,3}\)'

list = re.findall(regex, raw_text)

split_regex = '[(,)]'

def clean_mul(string_input: str) -> int:
    clean1 = re.split(split_regex, string_input)
    int_1, int_2 = int(clean1[1]), int(clean1[2])
    return int_1 * int_2

final = [clean_mul(elem) for elem in list]
print(sum(final))

