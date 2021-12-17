def part_one(file):
    with open(file, 'r') as input_fp:
        positions = [int(pos) for pos in input_fp.read().strip().split(',')]
    positions.sort()
    length = len(positions)
    if length % 2 != 0:
        target_pos = positions[length//2]
    else:
        right = positions[length//2]
        left = positions[length//2 - 1]
        target_pos = (right + left) // 2
    total_fuel = 0
    for pos in positions:
        total_fuel += abs(pos - target_pos)
    print(total_fuel)

part_one('.\\day7\\input.txt')

def part_two(file):
    with open(file, 'r') as input_fp:
        positions = [int(pos) for pos in input_fp.read().strip().split(',')]
    length = len(positions)
    total = sum(positions)
    target_position = sum(positions)//length #+ (total % length > 0)
    total_fuel = 0
    for pos in positions:
        num_steps = abs(pos - target_position)
        for i in range(1,num_steps + 1):
            total_fuel += i
    print(total_fuel)

part_two('.\\day7\\input.txt')