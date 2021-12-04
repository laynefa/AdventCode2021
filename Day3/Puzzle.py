def part_one():
    binary_data = []
    with open('.//Day3//input.txt', 'r') as binary_fp:
        for line in binary_fp:
            bits = []
            for bit in line.strip():
                bits.append(bit)
            binary_data.append(bits)
    #access by binary_data[0,0] then [1,0], [2,0], etc
    count0 = 0
    count1 = 0
    gamma_rate = ''
    epsilon_rate = ''
    for column in range(0, len(binary_data[0])): #columns
        for row in range(0, len(binary_data)): #rows
            bit = binary_data[row][column]
            if bit == '0':
                count0 += 1
            elif bit == '1':
                count1 += 1
            else:
                raise ValueError('Invalid bit value')
        if count0 > count1:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
        count0 = 0
        count1 = 0
    print('gamma rate: ' + gamma_rate)
    print('epsilon rate: ' + epsilon_rate)
    print('power consumption: ' + str(int(gamma_rate, 2) * int(epsilon_rate, 2)))
part_one()