from collections import defaultdict

def input_data_from_file(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    rules = defaultdict(set)
    updates = []
    rules_done = False
    for line in data:
        if line == '':
            rules_done = True
            continue
        if rules_done:
            updates.append(list(map(int, line.split(','))))
            continue
        else:
            x, y = (map(int, line.split('|')))
            rules[x].add(y)
    return rules, updates

def check_valid(rules, update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True

def fix_update(rules, update):
    new_rules = defaultdict(set)
    # filter new set of rules that are only relevant to values in current update
    for i in update:
        new_rules[i] = rules[i] & set(update)

    # order new update by the count of rules associated with that key. e.g. if x has more rules than y it appears earlier in the new list
    ordered_update = sorted(new_rules, key=lambda x: len(new_rules[x]), reverse=True)
    return ordered_update

if __name__ == '__main__':
    rules, updates = input_data_from_file('Advent_Day5_Input.txt')

    print(rules)
    print(updates)

    # part 1
    count=0
    for update in updates:
        if check_valid(rules, update):
            # its meant to be the sum of the middle silly bitch not just a count
            count += update[len(update) // 2]

    # part 2
    count=0
    for update in updates:
        if not check_valid(rules, update):
            fixed_update = fix_update(rules, update)
            count += fixed_update[len(fixed_update) // 2]
    print(count)
