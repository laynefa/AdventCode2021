open_to_close_chars = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

completion_points = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

def part_one(file):
    with open(file, 'r') as input_fp:
        lines = input_fp.read().splitlines()
    total = 0
    part_two_totals = []
    for line in lines:
        chars = []
        incomplete = True
        for char in line:
            if char in open_to_close_chars:
                chars.append(char)
            else:
                open_char = chars.pop()
                if open_to_close_chars[open_char] != char:
                    total += points[char]
                    incomplete = False
                    break
        if incomplete:
            part_two_total = 0
            closing_str = ''
            while(chars):
                char = chars.pop()
                required_end_char = open_to_close_chars[char]
                closing_str += required_end_char
                part_two_total = part_two_total * 5 + completion_points[required_end_char]
            part_two_totals.append(part_two_total)
    print('part one answer: ' + str(total))
    part_two_totals.sort()
    print('part two answer: ' + str(part_two_totals[len(part_two_totals) // 2]))

import time
start = time.perf_counter()
part_one('./Day10/input.txt')
end = time.perf_counter()
print('Complete in ' + str(end - start))
