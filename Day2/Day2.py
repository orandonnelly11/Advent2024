def input_data_from_file(filename):
    with open(filename) as f:
        out = f.read().splitlines()
        output = []
        for line in out:
            output.append(list(map(int, line.split())))
    return output

def check_duplicates(report):
    for level in report:
        if report.count(level) > 1:
            return True

def check_safe(report):
    if check_duplicates(report):
        return False
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    for i in range(len(report)):
        if i == len(report) - 1:
            continue
        if report[i] > report[i + 1]:
            if report[i] - report[i+1] > 3:
                return False
        elif report[i] < report[i + 1]:
            if report[i + 1] - report[i] > 3:
                return False
    return True

if __name__ == '__main__':
    data = input_data_from_file('Advent_Day2_Input.txt')
    #print(data)
    count = 0
    p2count = 0
    for row in data:
        if check_safe(row):
            count += 1

    for row in data:
        for i in range(len(row)):
            temp = row[:]
            temp.pop(i)
            if check_safe(temp):
                p2count += 1
                break

    print(count)
    print(p2count)


    #print(data)