def main():

    file_path = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day5/directions.txt'
    puzz_path = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day5/puzz.txt'

    with open(file_path, 'r') as file:
        raw_directions = file.readlines()

    with open(puzz_path, 'r') as file:
        puzz = file.readlines()

    final_puzz = []
    for line in puzz:
        clean = line.strip('\'').strip('\n').split(',')
        clean_2 = [int(item) for item in clean]
        final_puzz.append(clean_2)

    list_a = []
    for line in raw_directions:
        l = line.strip('\n')
        a = l.split("|")[0]
        b = l.split("|")[1]
        list_a.append(a)
        list_a.append(b)

    rule_list = []

    for line in raw_directions:
        l = line.strip('\n')
        a = [int(num) for num in l.split("|")]
        rule_list.append(a)

    total_valid = 0
    total_invalid = 0
    for row in final_puzz:
        raw_lst = fetch_rules(rule_list, row)
        print(raw_lst)
        rule_dct = populate_rule_dict(row, raw_lst)
        print(rule_dct) 
        order = gen_row_order(rule_dct, row)
        print(order)
        mid_row, mid_invalid = check_valid_list(order, row)
        print(mid_row)
        print(row)
        total_valid += mid_row
        total_invalid += mid_invalid

    print(total_valid, total_invalid)

def fetch_rules(mstr_list: list, row) -> list:
    row_rules = []
    for num in row:
        for idx, rule in enumerate(mstr_list):
            if num == mstr_list[idx][0]:
                row_rules.append(rule)
    return row_rules

def populate_rule_dict(keys: list, rules: list) -> dict:
    rule_dict = {k: [] for k in keys}
    for k, v in rule_dict.items():
        for i in rules:
            if k == i[0]:
                v.append(i[1])
        v.sort()
    final_rule_dict = {k: v for k, v in rule_dict.items() if len(v) > 0}
    return final_rule_dict

def gen_row_order(rules: dict, row_order: list) -> list:
    order = [num for num in row_order]
    for k, v in rules.items():
        curr_idx = order.index(k)
        for i in v:
            if i not in order:
                pass
            else:
                print(k)
                print(i)
                comp_idx = order.index(i)
                print(curr_idx)
                print(comp_idx)
                if curr_idx > comp_idx:
                    order[curr_idx], order[comp_idx] = order[comp_idx], order[curr_idx]
                    curr_idx = comp_idx
                    print(order)
        
    return order

def check_valid_list(order_list: list[int], candidate_list: list[int]) -> int:
    index_checker = [order_list.index(i) for i in candidate_list]
    print(index_checker)
    ascending = all(index_checker[i + 1] > index_checker[i] for i in range(len(index_checker) - 1))
    print(ascending)
    if ascending:
        midpoint = (len(index_checker) // 2) 
        print(midpoint)
        valid = candidate_list[midpoint]
        invalid = 0
    if not ascending:
        midpoint = (len(order_list) // 2) 
        print(midpoint)
        invalid = order_list[midpoint]
        valid = 0
    return valid, invalid

main()