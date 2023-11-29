def isValidSudoku(board):

    for row in board:
        num_set = set()
        for num in row:
            if num != ".":
                if num in num_set:
                    return "NO"
                num_set.add(num)

    for col in range(9):
        num_set = set()
        for row in board:
            num = row[col]
            if num != ".":
                if num in num_set:
                    return "NO"
                num_set.add(num)

    for i in range(3):
        for j in range(3):
            num_set = set()
            for m in range(3):
                for n in range(3):
                    num = board[i * 3 + m][j * 3 + n]
                    if num != ".":
                        if num in num_set:
                            return "NO"
                        num_set.add(num)

    return "YES"

def convertInputToBoard(input_str):
    rows = input_str.strip().split('\n')
    board = []

    for row in rows:
        row_values = row.split()
        board.append([int(val) if val.isdigit() else val for val in row_values])

    return board


input_str = """
5 3 . . 7 . . . .
5 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
"""


board = convertInputToBoard(input_str)
output = isValidSudoku(board)
print(output)