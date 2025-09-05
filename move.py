from typing import List


def _compress_row_left(row: List[int]) -> List[int]:
    """Remove zeros while preserving order."""
    return [x for x in row if x != 0]


def _merge_row_left(row: List[int]) -> List[int]:
    """
    Given a zero-free row (e.g., after compress), merge equal adjacent tiles once,
    scanning left to right. Returns the merged (still zero-free) row.
    """
    merged = []
    i = 0
    while i < len(row):
        if i + 1 < len(row) and row[i] == row[i + 1]:
            merged.append(row[i] * 2)
            i += 2  # skip the next tile (it's consumed)
        else:
            merged.append(row[i])
            i += 1
    return merged


def move_left(board: List[List[int]]) -> List[List[int]]:
    """
    Apply a 2048 LEFT move to the entire grid.
    Steps per row: compress -> merge -> compress -> pad zeros to the right.
    """
    n = len(board)
    result = []
    for r in range(n):
        row = board[r]
        step1 = _compress_row_left(row)
        step2 = _merge_row_left(step1)
        step3 = _compress_row_left(step2)
        # pad with zeros on the right
        padded = step3 + [0] * (n - len(step3))
        result.append(padded)
    return result


# --- Optional stdin driver the interviewer might expect ---
# Input format:
# n
# <n lines of n integers>
if __name__ == "__main__":
    import sys

    data = sys.stdin.read().strip().split()
    if data:
        it = iter(data)
        n = int(next(it))
        board = [[int(next(it)) for _ in range(n)] for _ in range(n)]
        moved = move_left(board)
        for row in moved:
            print(*row)
