def part1(file):
    #grid = [[0]*10 for i in range(10)]
    plotted_points = set()
    repeats = set()
    multiples = 0
    with open(file, 'r') as file_fp:
        for line in file_fp:
            line = line.strip()
            first_coord, second_coord = line.split('->')
            first_coord = first_coord.strip()
            second_coord = second_coord.strip()
            x1,y1 = [int(coord) for coord in first_coord.split(',')]
            x2,y2 = [int(coord) for coord in second_coord.split(',')]
            points = []
            if x1 == x2: #vertical line
                if y1 >= y2:
                    start = y2
                    stop = y1
                else:
                    start = y1
                    stop = y2
                for i in range(start, stop + 1):
                    points.append((x1,i))
            elif y1 == y2: #horizontal line
                if x1 >= x2:
                    start = x2
                    stop = x1
                else:
                    start = x1
                    stop = x2
                for i in range(start, stop + 1):
                    points.append((i,y1))
            for point in points:
                x,y = point
                if point in plotted_points and point not in repeats:
                    multiples += 1
                    repeats.add(point)
                plotted_points.add(point)
                #grid[y][x] += 1
    print(multiples)
    #for row in grid:
    #    print(row)

part1('./Day5/input.txt')