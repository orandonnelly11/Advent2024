from collections import defaultdict

DIR_MAPPINGS = {
    "NORTH": [-1, 0, 'N'],
    "SOUTH": [1, 0, 'S'],
    "WEST": [0, -1, 'W'],
    "EAST": [0, 1, 'E']
}

def read_data_from_file(filename="Advent_Day6_Input.txt"):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = [list(line.strip()) for line in lines]
    starting_pos = None
    for i, row in enumerate(data):
        if '^' in row:
            starting_pos = [i, row.index('^')]
            break
    return data, starting_pos

def part_one(data, starting_pos):
    visited = defaultdict(set)
    add_to_map(visited, ','.join(map(str, starting_pos)), 'N')

    is_out_of_bounds = False
    current_pos = starting_pos
    direction = DIR_MAPPINGS["NORTH"]

    while not is_out_of_bounds:
        next_row = current_pos[0] + direction[0]
        next_col = current_pos[1] + direction[1]
        look_ahead = get_space(data, next_row, next_col)

        if look_ahead == 'OOB':
            is_out_of_bounds = True
        elif look_ahead == '#':
            direction = determine_new_direction(direction)
        else:
            key = ','.join(map(str, [next_row, next_col]))
            if direction[2] in visited.get(key, set()):
                return 'LOOP'

            current_pos = [next_row, next_col]
            add_to_map(visited, key, direction[2])

    return visited

def part_2_pls_work(data, starting_pos):
    blocks = part_one(data, starting_pos)
    blocks.pop(','.join(map(str, starting_pos)), None)

    loops_count = 0

    for key, _ in blocks.items():
        row, col = map(int, key.split(','))
        data[row][col] = '#'

        if part_one(data, starting_pos) == 'LOOP':
            loops_count += 1

        data[row][col] = '.'

    print(loops_count)

def add_to_map(map, key, value):
    map[key].add(value)

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
    data, starting_pos = read_data_from_file()
    print(len(part_one(data, starting_pos)))
    print(part_2_pls_work(data, starting_pos))