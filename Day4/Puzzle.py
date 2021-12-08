class Board():
    def __init__(self, board_contents):
        self.bingo_board = []
        self.sum = 0
        for line in board_contents:
            row = []
            for i in range(0, 14, 3):
                value = int(line[i:i+2].strip())
                self.sum += value
                row.append(value)
            self.bingo_board.append(row)
            

    def mark_number(self, number):
        pass

    def check_win(self):
        pass

if __name__ == '__main__':
    with open('./Day4/sample_numbers.txt', 'r') as numbers_file, open('./Day4/sample_boards.txt') as boards_file:
        numbers = [int(num) for num in numbers_file.read().strip().split(',')]
        boards = []
        board = []
        for line in boards_file:
            line = line.rstrip()
            if not line:
                boards.append(Board(board))
                board = []
            else:
                board.append(line)
    print(numbers)
    print(boards)