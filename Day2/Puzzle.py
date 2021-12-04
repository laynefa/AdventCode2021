def part_one():
    horizontal = 0
    depth = 0
    with open('.//Day2//input.txt', 'r') as directions_data:
        for line in directions_data:
            direction, units = line.strip().split(' ')
            units = int(units)
            if direction == 'forward':
                horizontal += units
            elif direction == 'down':
                depth += units
            elif direction == 'up':
                depth -= units
            else:
                raise ValueError('Unknown direction of ' + direction)
    print('horizontal: ' + str(horizontal))
    print('depth: ' + str(depth))
    print('horizontal*depth: ' + str(horizontal*depth))

def part_two():
    horizontal = 0
    depth = 0
    aim = 0
    with open('.//Day2//input.txt', 'r') as directions_data:
        for line in directions_data:
            direction, units = line.strip().split(' ')
            units = int(units)
            if direction == 'forward':
                horizontal += units
                depth += aim*units
            elif direction == 'down':
                aim += units
            elif direction == 'up':
                aim -= units
            else:
                raise ValueError('Unknown direction of ' + direction)
    print('horizontal: ' + str(horizontal))
    print('depth: ' + str(depth))
    print('aim: ' + str(aim))
    print('horizontal*depth: ' + str(horizontal*depth))

part_one()
print()
part_two()