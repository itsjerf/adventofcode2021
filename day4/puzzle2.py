from pprint import pprint
import sys

def read_input():
    inputfile = "input.txt"
    data = {}
    data["boards"] = {}
    with open(inputfile, 'r') as f:
        board_counter = 0
        for idx, line in enumerate(f):
            if idx == 0:
                n = line.strip("\n")
                n = [int(x) for x in n.split(",")]
                data["numbers"] = n
            elif line == "\n":
                board_counter += 1
                data["boards"][board_counter] = []
            else:
                d = line.strip("\n").split(" ")
                d = [int(x) for x in d if x]
                data["boards"][board_counter].append(d)
    return data

def calc_win(board, numbers):
    values = []
    for i in range(len(board[0])):
        for row in board:
            if row[i] not in numbers:
                values.append(row[i])
    win_result = sum(values) * numbers[-1]
    return win_result

def check_win(board, numbers):
    results = [
        check_rows(board, numbers),
        check_columns(board, numbers)
    ]
    if any(results):
        # msg = ""
        # if results[0]:
        #     msg = "ROW win"
        # if results[1]:
        #     msg = "COLUMN win"
        # print(msg)
        return calc_win(board, numbers)
    return None

def check_rows(board, numbers):
    for row in board:
        result = all(i in numbers for i in row)
        if result:
            return True
    return False

def check_columns(board, numbers):
    columns = []
    for i in range(len(board[0])):
        c = []
        for row in board:
            c.append(row[i])
        columns.append(c)
    for column in columns:
        result = all(i in numbers for i in column)
        if result:
            return True
    return False

def check_diags(board, numbers):
    diags = []
    fdiag = []
    bdiag = []
    fdiag_indices = [(0,0), (1,1), (2,2), (3,3), (4,4)]
    bdiag_indices = [(0,4), (1,3), (2,2), (3,1), (4,0)]
    for (r, i) in fdiag_indices:
        fdiag.append(board[r][i])
    for (r, i) in bdiag_indices:
        bdiag.append(board[r][i])
    diags.append(fdiag)
    diags.append(bdiag)
    for diag in diags:
        result = all(i in diag for i in numbers)
        if result:
            return True
    return False

def main():
    data = read_input()
    numbers = data["numbers"]
    boards = data["boards"]
    active_numbers = []
    active_numbers.extend(numbers[:4])
    winners_idx = []
    winners_scores = {}
    for n in numbers[4:]:
        active_numbers.append(n)
        for idx, b in boards.items():
            result = check_win(b, active_numbers)
            if result:
                if idx not in winners_idx:
                    winners_idx.append(idx)
                    winners_scores[idx] = result
    # winners = list(set(winners))
    print(f"Winning boards: {winners_idx}")
    print(f"Last winning board: {winners_idx[-1]}")
    for row in boards[winners_idx[-1]]:
        print(row)
    print(f"Last winning board score: {winners_scores[winners_idx[-1]]}")
if __name__ == '__main__':
    main()