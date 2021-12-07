def part_one():
    binary_data = []
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
    print('gamma rate: ' + gamma_rate)
    print('epsilon rate: ' + epsilon_rate)
    print('power consumption: ' + str(int(gamma_rate, 2) * int(epsilon_rate, 2)))

def part_two():
    binary_data = []
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
    print('gamma rate: ' + gamma_rate)
    print('epsilon rate: ' + epsilon_rate)
    print('power consumption: ' + str(int(gamma_rate, 2) * int(epsilon_rate, 2)))

part_one()