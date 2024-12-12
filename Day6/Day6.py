from collections import defaultdict

DIR_MAPPINGS = {
    "NORTH": [-1, 0, 'N'],
    "SOUTH": [1, 0, 'S'],
    "WEST": [0, -1, 'W'],
    "EAST": [0, 1, 'E']
}

def read_data_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = [list(line.strip()) for line in lines]
    starting_pos = None
    for i, row in enumerate(data):
        if '^' in row:
            starting_pos = [i, row.index('^')]
            break
    return data, starting_pos

def navigate_data(data, starting_pos):
    visited = defaultdict(set)
    current_pos = starting_pos
    direction = DIR_MAPPINGS["NORTH"]
    path = [(current_pos[0], current_pos[1], direction[2])]

    while True:
        next_row = current_pos[0] + direction[0]
        next_col = current_pos[1] + direction[1]
        look_ahead = get_space(data, next_row, next_col)

        if look_ahead == 'OOB':
            break
        elif look_ahead == '#':
            direction = determine_new_direction(direction)
        else:
            key = (next_row, next_col)
            if direction[2] in visited[key]:
                return 'LOOP', path
            visited[key].add(direction[2])
            current_pos = [next_row, next_col]
            path.append((current_pos[0], current_pos[1], direction[2]))

    return 'NO_LOOP', path

def part_one(data, starting_pos):
    result, path = navigate_data(data, starting_pos)
    return len(path) if result == 'NO_LOOP' else 'LOOP'

def part_two(data, starting_pos):
    _, path = navigate_data(data, starting_pos)
    loops_count = 0

    for i in range(1, len(path)):
        row, col, _ = path[i]
        data[row][col] = '#'
        result, _ = navigate_data(data, starting_pos)
        if result == 'LOOP':
            loops_count += 1
        data[row][col] = '.'

    print(loops_count)

def determine_new_direction(direction):
    if direction == DIR_MAPPINGS["NORTH"]:
        return DIR_MAPPINGS["EAST"]
    elif direction == DIR_MAPPINGS["EAST"]:
        return DIR_MAPPINGS["SOUTH"]
    elif direction == DIR_MAPPINGS["SOUTH"]:
        return DIR_MAPPINGS["WEST"]
    elif direction == DIR_MAPPINGS["WEST"]:
        return DIR_MAPPINGS["NORTH"]

def get_space(data, row, col):
    if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]):
        return 'OOB'
    return data[row][col]

if __name__ == "__main__":
    data, starting_pos = read_data_from_file("Advent_Day6_Input.txt")
    print(part_one(data, starting_pos))
    part_two(data, starting_pos)