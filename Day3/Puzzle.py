def part_one():
    with open('.//Day3//input.txt', 'r') as binary_fp:
        first_line = binary_fp.readline().strip()
        counts0 = []
        counts1 = []
        size = len(first_line)
        for i in range(size):
            if first_line[i] == '0':
                counts0.append(1)
                counts1.append(0)
            else:
                counts1.append(1)
                counts0.append(0)
        for line in binary_fp:
            line = line.strip()
            for bit_count, bit in enumerate(line):
                if bit == '0':
                    counts0[bit_count] += 1
                else:
                    counts1[bit_count] += 1
        gamma_rate = ''
        epsilon_rate = ''
        for i in range(size):
            if counts0[i] > counts1[i]:
                gamma_rate += '0'
                epsilon_rate += '1'
            else:
                gamma_rate += '1'
                epsilon_rate += '0'
    print('counts0: ' + str(counts0))
    print('counts1: ' + str(counts1))
    print('gamma rate: ' + gamma_rate)
    print('epsilon rate: ' + epsilon_rate)
    print('power consumption: ' + str(int(gamma_rate, 2) * int(epsilon_rate, 2)))

def get_filter_critera(binary_data, bit_position, operation):
    counts0 = 0
    counts1 = 0
    zero_locations = set()
    ones_locations = set()
    for count, data in enumerate(binary_data):
        if data[bit_position] == '0':
            counts0 += 1
            zero_locations.add(count)
        else:
            counts1 += 1
            ones_locations.add(count)
    if operation == 'oxygen':
        if counts1 >= counts0:
            return ones_locations
        else:
            return zero_locations
    else:
        if counts0 <= counts1:
            return zero_locations
        else:
            return ones_locations

def filter_values(binary_data, bit_position, operation):
    remaining_values = []
    for location in get_filter_critera(binary_data, bit_position, operation):
        remaining_values.append(binary_data[location])
    return remaining_values

def part_two():
    with open('.//Day3//input.txt', 'r') as binary_fp:
        binary_data = binary_fp.read().splitlines()
    oxygen_rating = binary_data
    co2_rating = binary_data
    bit_position = 0
    while(len(oxygen_rating) != 1):
        oxygen_rating = filter_values(oxygen_rating, bit_position, 'oxygen')
        bit_position += 1
    bit_position = 0
    while(len(co2_rating) != 1):
        co2_rating = filter_values(co2_rating, bit_position, 'co2')
        bit_position += 1
    print(str(int(oxygen_rating[0],2) * int(co2_rating[0], 2)))

part_one()
part_two()