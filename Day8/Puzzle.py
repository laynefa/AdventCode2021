"""
find 3 by getting rid of 7's letters in it from
the numbers that have 5 letters. if there are 
two letters left, then its 3

find 5 by removing 4's letters from the numbers
that have 5 letters left. if there are 2 letters left,
then its 5

remaining one would be 2

find 9 by removing 4's letters from numbers that
have 6 letters. if there are 2 letters remaining,
its 9

find 0 by removing 5's letters. if 2 left over, its 0

remaining number would be 6

remaining is 8
"""

def part_one(file):
    count = 0
    with open(file, 'r') as input_fp:
        for line in input_fp:
            input, output = line.strip().split(' | ')
            outputs = output.split(' ')
            for output in outputs:
                if len(output) in [2,3,4,7]:
                    count += 1
    print(count)

def part_two(file):
    total = 0
    with open(file, 'r') as input_fp:
        for line in input_fp:
            str_total = ''
            input, output = line.strip().split(' | ')
            temp_inputs = input.split(' ')
            inputs = []
            for i in temp_inputs:
                inputs.append(''.join(sorted(i)))
            outputs = output.split(' ')
            inputs.sort(key=len)
            letter_mapping = {}
            number_mapping = {}
            letter_mapping[inputs[0]] = 1
            letter_mapping[inputs[1]] = 7
            letter_mapping[inputs[2]] = 4
            letter_mapping[inputs[-1]] = 8
            number_mapping[1] = inputs[0]
            number_mapping[7] = inputs[1]
            number_mapping[4] = inputs[2]
            number_mapping[8] = inputs[-1]
            found = inputs[3:6].copy()
            while len(found) > 1:
                for i in found:
                    if len(set(i) - set(number_mapping[7])) == 2:
                        letter_mapping[i] = 3
                        number_mapping[3] = i
                        found.remove(i)
                        break
                    elif len(set(i) - set(number_mapping[4])) == 2:
                        letter_mapping[i] = 5
                        number_mapping[5] = i
                        found.remove(i)
                        break
            letter_mapping[found[0]] = 2
            number_mapping[2] = found[0]
            found = inputs[6:9].copy()
            while len(found) > 1:
                for i in found:
                    if len(set(i) - set(number_mapping[4])) == 2:
                        letter_mapping[i] = 9
                        number_mapping[9] = i
                        found.remove(i)
                        break
                    elif len(set(i) - set(number_mapping[5])) == 2:
                        letter_mapping[i] = 0
                        number_mapping[0] = i
                        found.remove(i)
                        break
            letter_mapping[found[0]] = 6
            number_mapping[6] = found[0]
            for output in outputs:
                str_total += str(letter_mapping[''.join(sorted(output))])
            total += int(str_total)
    print(total)

part_one('./day8/input.txt')
part_two('./day8/input.txt')