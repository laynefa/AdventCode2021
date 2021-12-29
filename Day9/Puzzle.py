def calculate_basin(row_num, col_num, height_map, calculate_map, data_length, total_data_rows):
    col_value = height_map[row_num][col_num]
    if col_value == 9 or col_value == 'x':
        return 0
    height_map[row_num][col_num] = 'x'
    calculate_map[row_num][col_num] = False
    basin_size = 1
    if col_num != 0: #check left
        basin_size += calculate_basin(row_num, col_num - 1, height_map, calculate_map, data_length, total_data_rows)
    if col_num != data_length - 1: #check right
        basin_size += calculate_basin(row_num, col_num + 1, height_map, calculate_map, data_length, total_data_rows)
    if row_num != 0: #check up
        basin_size += calculate_basin(row_num - 1, col_num, height_map, calculate_map, data_length, total_data_rows)
    if row_num != total_data_rows - 1: #check down
        basin_size += calculate_basin(row_num + 1, col_num, height_map, calculate_map, data_length, total_data_rows)
    return basin_size

def part_one(file):
    height_map = []
    calculate_map = []
    data_length = 0
    total_data_rows = 0
    with open(file, 'r') as fp:
        for line in fp:
            total_data_rows += 1
            line = line.strip()
            data_length = len(line)
            calculate_map.append([True]*data_length)
            row = []
            for value in line:
                row.append(int(value))
            height_map.append(row)
    risk_level = 0
    basins = []
    basin_size = 0
    for row_num, row in enumerate(height_map):
        for col_num, col_value in enumerate(row):
            if col_value != 9 and calculate_map[row_num][col_num]:
                if col_num != 0: #check left
                    if col_value >= row[col_num - 1]:
                        continue
                if col_num != data_length - 1: #check right
                    if col_value >= row[col_num + 1]:
                        continue
                    else:
                        calculate_map[row_num][col_num + 1] = False
                if row_num != 0: #check up
                    if col_value >= height_map[row_num - 1][col_num]:
                        continue
                if row_num != total_data_rows - 1: #check down
                    if col_value >= height_map[row_num + 1][col_num]:
                        continue
                    else:
                        calculate_map[row_num + 1][col_num] = False
                risk_level += 1 + col_value
                basins.append(calculate_basin(row_num, col_num, height_map, calculate_map, data_length, total_data_rows))
    print(risk_level)
    basins.sort()
    print(basins)
    print(str(basins[-1] * basins[-2] * basins[-3]))
import time
start = time.perf_counter()
part_one('./Day9/input.txt')
end = time.perf_counter()
print('Complete in ' + str(end - start))