import re

def input_data_from_file(filename):
    with open(filename) as f:
        out = f.read().replace('\n','')
    return out

if __name__ == '__main__':
    data = input_data_from_file('Advent_Day3_Input.txt')
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', data)

    #part1
    count = 0
    for match in matches:
        if re.search(r'do\(\)', match):
            continue
        elif re.search(r'don\'t\(\)', match):
            continue
        else:
            x, y = int(match.split(',')[0].strip('mul(')), int(match.split(',')[1].strip(')'))
            count += (x * y)

    print(count)

    # part2
    count = 0
    do = True
    for match in matches:
        if re.search(r'do\(\)', match):
            do = True
        elif re.search(r'don\'t\(\)', match):
            do = False
        elif do:
            x, y = int(match.split(',')[0].strip('mul(')), int(match.split(',')[1].strip(')'))
            count += (x * y)

    print(count)
