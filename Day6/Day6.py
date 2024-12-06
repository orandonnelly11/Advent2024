from collections import defaultdict

def read_data_from_file(filename):
    with open(filename) as f:
        out = f.read().splitlines()
        output = []
        for line in out:
            output.append(list(line))
    return output

def get_start(data):
    for i in range(len(data)):
        line = data[i]
        if line.count('^'):
            for j in range(len(line)):
                if line[j] == '^':
                    return i, j

def check_ahead(data, row, col):
    if data[row][col] == '.' or data[row][col] == 'X':
        return True
    return False

def traverse(data, row, col):
    valid_steps = 0
    loop_cnt = 0
    visited = set()

    finished = False
    while len(data) > row > 0 and len(data[0]) > col > 0:
        if data[row][col] == '^':
            if check_ahead(data, row - 1, col):
                if data[row-1][col] != 'X':
                    valid_steps+=1
                if (row,col,'^') in visited:
                    loop_cnt+=1
                visited.add((row,col,'^'))
                data[row][col] = 'X'
                row -= 1
                data[row][col] = '^'
                if (row,col,'^') in visited:
                    loop_cnt+=1
                visited.add((row,col,'^'))
            else:
                data[row][col] = '>'
        elif data[row][col] == '>':
            if check_ahead(data, row, col + 1):
                if data[row][col+1] != 'X':
                    valid_steps+=1
                if (row,col,'>') in visited:
                    loop_cnt+=1
                    break
                visited.add((row,col,'>'))
                data[row][col] = 'X'
                col += 1
                data[row][col] = '>'
            else:
                data[row][col] = 'v'
        elif data[row][col] == '<':
            if check_ahead(data, row , col - 1):
                if data[row][col-1] != 'X':
                    valid_steps+=1
                if (row,col,'<') in visited:
                    loop_cnt+=1
                visited.add((row,col,'<'))
                data[row][col] = 'X'
                col -= 1
                data[row][col] = '<'
            else:
                data[row][col] = '^'
        elif data[row][col] == 'v':
            if check_ahead(data, row + 1, col):
                if data[row+1][col] != 'X':
                    valid_steps+=1
                if (row,col,'v') in visited:
                    loop_cnt+=1
                visited.add((row,col,'v'))
                data[row][col] = 'X'
                row += 1
                data[row][col] = 'v'
            else:
                data[row][col] = '<'

    data[row][col] = 'X'
    valid_steps+=1
    return valid_steps, loop_cnt

if __name__ == '__main__':
    data = read_data_from_file('Advent_Day6_Input.txt')
    #print(data)
    start_row, start_col = get_start(data)
    print(traverse(data, start_row, start_col))

