def count_xmas(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal Up-Left
        (-1, 1)   # Diagonal Up-Right
    ]
    target = "XMAS"
    target_len = len(target)
    count = 0

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                # Check if the word fits in this direction
                if 0 <= row + dr * (target_len - 1) < rows and \
                   0 <= col + dc * (target_len - 1) < cols:
                    # Check the word in this direction
                    word = ''.join(grid[row + i * dr][col + i * dc] for i in range(target_len))
                    if word == target:
                        count += 1

    return count


# Read and process the input files
file_path = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day4/raw.txt'
test_file = '/Users/davidshames/python-projects/advent-of-code/advent_of_code/day4/test.txt'

with open(file_path, 'r') as file:
    raw_text = [line.strip() for line in file.readlines()]

with open(test_file, 'r') as file:
    raw_test = [line.strip() for line in file.readlines()]

# Test the function
test_count = count_xmas(raw_test)
print(f"Number of XMAS in test grid: {test_count}")

# Full input
input_count = count_xmas(raw_text)
print(f"Number of XMAS in full grid: {input_count}")
