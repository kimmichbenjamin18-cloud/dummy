from typing import List, Literal

Direction = Literal["LEFT", "RIGHT", "UP", "DOWN"]

def _compress_row_left(row: List[int]) -> List[int]:
    return [x for x in row if x != 0]

def _merge_row_left(row: List[int]) -> List[int]:
    merged = []
    i = 0
    while i < len(row):
        if i + 1 < len(row) and row[i] == row[i + 1]:
            merged.append(row[i] * 2)
            i += 2  # consume the next tile
        else:
            merged.append(row[i])
            i += 1
    return merged

def _pad_right(row: List[int], n: int) -> List[int]:
    return row + [0] * (n - len(row))

def move_left(board: List[List[int]]) -> List[List[int]]:
    n = len(board)
    out = []
    for row in board:
        step1 = _compress_row_left(row)
        step2 = _merge_row_left(step1)
        step3 = _compress_row_left(step2)
        out.append(_pad_right(step3, n))
    return out

# --- simple transforms to reuse move_left ---
def _reverse_rows(board: List[List[int]]) -> List[List[int]]:
    return [list(reversed(row)) for row in board]

def _transpose(board: List[List[int]]) -> List[List[int]]:
    # assumes square board
    return [list(col) for col in zip(*board)]

def move(board: List[List[int]], direction: Direction) -> List[List[int]]:
    """
    Apply a 2048 move in the given direction to a square board.
    """
    if direction == "LEFT":
        return move_left(board)
    elif direction == "RIGHT":
        # reverse rows -> left -> reverse back
        return _reverse_rows(move_left(_reverse_rows(board)))
    elif direction == "UP":
        # transpose -> left -> transpose back
        return _transpose(move_left(_transpose(board)))
    elif direction == "DOWN":
        # transpose -> right -> transpose back
        trans = _transpose(board)
        moved = _reverse_rows(move_left(_reverse_rows(trans)))
        return _transpose(moved)
    else:
        raise ValueError("Invalid direction. Use LEFT, RIGHT, UP, or DOWN.")

# --- Optional stdin driver ---
# Input:
# n
# <n lines>
# DIRECTION (e.g., LEFT/RIGHT/UP/DOWN)
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().strip().split()
    if tokens:
        it = iter(tokens)
        n = int(next(it))
        grid = [[int(next(it)) for _ in range(n)] for _ in range(n)]
        direction = next(it).upper() if tokens[-1].isalpha() else "LEFT"
        result = move(grid, direction)
        for r in result:
            print(*r)
