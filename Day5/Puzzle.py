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
                start = min(y1,y2)
                stop = max(y1,y2)
                for i in range(start, stop + 1):
                    points.append((x1,i))
            elif y1 == y2: #horizontal line
                start = min(x1,x2)
                stop = max(x1,x2)
                for i in range(start, stop + 1):
                    points.append((i,y1))
            else:
                x_steps = x1 - x2
                y_steps = y1 - y2
                if x_steps >= 0:
                    x_step = -1
                else:
                    x_step = 1
                if y_steps >= 0:
                    y_step = -1
                else:
                    y_step = 1
                while(x1 != x2):
                    points.append((x1, y1))
                    x1 += x_step
                    y1 += y_step
                points.append((x1, y1))
            for point in points:
                if point in plotted_points and point not in repeats:
                    multiples += 1
                    repeats.add(point)
                plotted_points.add(point)
    print(multiples)

part1('./Day5/input.txt')