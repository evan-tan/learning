"""Hackerrank Problems"""


def staircase(n):
    """Print right justified staircase usings spaces and hashes"""
    for row in range(n):
        n_hashes = row + 1
        n_spaces = n - n_hashes
        print(" " * n_spaces, end="")
        print("#" * n_hashes)
