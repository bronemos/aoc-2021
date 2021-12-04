with open("input.txt") as f:
    puzzle_in = f.read().split("\n" * 2)

draws = list(map(int, puzzle_in[0].split(",")))
boards_rows = [
    [
        list(map(int, row.split()))
        for row in board.split("\n")
        if len(set(row.split())) > 0
    ]
    for board in puzzle_in[1:]
]

boards_columns = [list(map(list, zip(*row))) for row in boards_rows]

draw_set = set()
found = False
for draw in draws:
    draw_set.add(draw)
    for board_rows, board_columns in zip(boards_rows, boards_columns):
        for row, column in zip(board_rows, board_columns):
            if set(row).issubset(draw_set):
                print(
                    sum(set([num for row in board_rows for num in row]) - draw_set)
                    * draw
                )
                found = True
                break
            elif set(column).issubset(draw_set):
                print(
                    sum(
                        set([num for column in board_columns for num in column])
                        - draw_set
                    )
                    * draw
                )
                found = True
                break
    if found:
        break

drawn = 0
while drawn < len(draws) + 1 and len(boards_rows) > 0:
    drawn += 1
    draw_set = set(draws[:drawn])
    for board_rows, board_columns in zip(boards_rows, boards_columns):
        found = False
        for row, column in zip(board_rows, board_columns):
            if set(row).issubset(draw_set):
                found = True
                score = (
                    sum(set([num for row in board_rows for num in row]) - draw_set)
                    * draws[drawn - 1]
                )
                break
            elif set(column).issubset(draw_set):
                found = True
                score = (
                    sum(
                        set([num for column in board_columns for num in column])
                        - draw_set
                    )
                    * draws[drawn - 1]
                )
                break
        if found:
            boards_rows.remove(board_rows)
            boards_columns.remove(board_columns)

print(score)

