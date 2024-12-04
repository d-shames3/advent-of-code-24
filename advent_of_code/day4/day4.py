file_path = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day4/raw.txt'
test_file = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day4/test.txt'


with open(file_path, 'r') as file:
    raw_text = file.readlines()

with open(test_file, 'r') as file:
    raw_test = file.readlines()

def gen_matrix(txt) -> list[list]:
    matrix = [line.strip('\n') for line in txt]
    return matrix

def pull_square(lst: list, row_idx: int, col_idx: int) -> str:
    square = []
    row = row_idx
    for i in range(4):
        my_slice = slice(col_idx, col_idx + 4)
        square.append(lst[row][my_slice])
        row += 1
    return square

def check_across(lst: list[str]) -> int:
    xmas_x = 0
    for row in lst:
        if row == 'XMAS' or row[::-1] == 'XMAS':
            xmas_x += 1
    return xmas_x

def check_vert(lst: list[str]) -> int:
    xmas_v = 0
    col = []
    for i in range(4):
        string = ''
        for j in range(4):
            pivot_col = lst[j][i]
            string = string + pivot_col
        col.append(string)
    for row in col:
        if row == 'XMAS' or row[::-1] == 'XMAS':
            xmas_v += 1
    return xmas_v

def check_diag(lst: list[str]) -> int: 
    xmas_d = 0
    col = []
    for i in range(4):
        if i == 0:
            string = ''
            idx = 0
            for j in range(4):
                pivot_col = lst[idx][idx]
                string = string + pivot_col
                idx += 1
            col.append(string)
        elif i == 3:
            string = ''
            idx = 3
            for j in range(4):
                pivot_col = lst[j][idx]
                string = string + pivot_col
                idx -= 1
            col.append(string)
    for row in col:
        if row == 'XMAS' or row[::-1] == 'XMAS':
            xmas_d += 1
    return xmas_d            


test = gen_matrix(raw_test)
print(test)

combos = []
row = 0
for i in range(7):
    col = 0
    for j in range(7):
        print(row, col)
        square = pull_square(test, row, col)
        combos.append(square)
        col += 1
    row += 1

print(combos)

xmas_counter = 0
for idx, combo in enumerate(combos):
    print(idx)
    x = check_across(combo)
    y = check_vert(combo)
    z = check_diag(combo)
    print(x, y, z)
    xmas_counter += x + y + z

print(xmas_counter)

testing = pull_square(test, 0, 5)
t2 = check_across(testing)
t3 = check_vert(testing)
t4 = check_diag(testing)
print(testing)
print(t2)
print(t3)
print(t4)
