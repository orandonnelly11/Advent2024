def input_data_from_file(filename):
    with open(filename, 'r') as f:
        input_txt = f.read().splitlines()
    return input_txt

if __name__ == '__main__':

    left_list_of_ins = []
    right_list_of_ins = []
    input_txt = input_data_from_file('InputDay1_Part1.txt')
    # print(input_txt)

    for line in input_txt:
        split = line.split('   ')
        left_list_of_ins.append(int(split[0]))
        right_list_of_ins.append(int(split[1]))

    left_list_of_ins = sorted(left_list_of_ins)
    right_list_of_ins = sorted(right_list_of_ins)
    # print(left_list_of_ins)
    # print(right_list_of_ins)

    overall_distance = 0
    current_distance = 0
    for i in range(len(left_list_of_ins)):
        if left_list_of_ins[i] < right_list_of_ins[i]:
            current_distance = right_list_of_ins[i] - left_list_of_ins[i]
        elif right_list_of_ins[i] < left_list_of_ins[i]:
            current_distance = left_list_of_ins[i] - right_list_of_ins[i]
        # print(current_distance)
        overall_distance += current_distance
        current_distance = 0

    # print(overall_distance)
    similarity_score = 0
    occurrence_count = 0
    for num in left_list_of_ins:
        occurrence_count = right_list_of_ins.count(num)
        # print(occurrence_count)
        similarity_score += (num * occurrence_count)
    print(similarity_score)


    similarity_score = 0
    for i in range(len(left_list_of_ins)):
        occurrence_count = 0
        for j in range(len(right_list_of_ins)):
            if left_list_of_ins[i] == right_list_of_ins[j]:
                occurrence_count += 1
        similarity_score += (left_list_of_ins[i] * occurrence_count)
    print(similarity_score)

