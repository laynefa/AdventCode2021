import os

def part_one():
    with open('.\\Day1\\input.txt', 'r') as readings_data:
        current_value = int(readings_data.readline().strip())
        increase_count = 0
        for reading in readings_data:
            new_value = int(reading.strip())
            if new_value > current_value:
                increase_count += 1
            current_value = new_value
    print(increase_count)

def part_two():
    input_data = []
    with open('.\\Day1\\input.txt', 'r') as readings_data:
        for reading in readings_data:
            input_data.append(int(reading.strip()))
    increase_count = 0
    input_size = len(input_data)
    #first frame
    left = input_data[0]
    middle = input_data[1]
    right = input_data[2]
    current_sum = left + middle + right
    #shift down one
    ptr2 = 3
    while ptr2 <= input_size - 1:
        new_right = input_data[ptr2]
        new_sum = current_sum - left + new_right
        if new_sum > current_sum:
            increase_count += 1
        ptr2+=1
        current_sum = new_sum
        left = middle
        middle = right
        right = new_right
    print(increase_count)
    
part_one()
part_two()
