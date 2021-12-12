class Board():
    def __init__(self, board_contents):
        self.bingo_board = []
        self.sum = 0
        self.locations = {}
        self.row_count = [0,0,0,0,0]
        self.column_count = [0,0,0,0,0]
        self.won = False
        for row_num, line in enumerate(board_contents):
            row = []
            for col_num, i in enumerate(range(0, 14, 3)):
                value = int(line[i:i+2].strip())
                self.sum += value
                row.append(value)
                self.locations[value] = (row_num, col_num)
            self.bingo_board.append(row)
            
    def mark_number(self, number):
        if not self.won and number in self.locations:
            self.sum -= number
            row,col = self.locations[number]
            row_marks = self.row_count[row]
            col_marks = self.column_count[col]
            if row_marks == 4 or col_marks == 4:
                self.won = True
                return True
            self.row_count[row] = row_marks + 1
            self.column_count[col] = col_marks + 1

    def print_board(self):
        print(self.bingo_board)

    def print_score(self, number):
        print(self.sum * number)
                
def main(numbers, boards):
    last_board = 0
    boards_won = 0
    total_boards = len(boards)
    number = None
    for number in numbers:
        for count, board in enumerate(boards):
            if board.mark_number(number):
                if boards_won == 0:
                    print('Board #' + str(count+1) + ' is the first to win')
                    board.print_board()
                    board.print_score(number)
                boards_won += 1
                if boards_won == total_boards:
                    last_board = count
                    break
        if boards_won == total_boards:
            break
    print('last board to win is board #' + str(last_board+1))
    boards[last_board].print_board()
    boards[last_board].print_score(number)

if __name__ == '__main__':
    with open('./Day4/numbers.txt', 'r') as numbers_file, open('./Day4/boards.txt') as boards_file:
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
        boards.append(Board(board))
    print(numbers)
    main(numbers, boards)