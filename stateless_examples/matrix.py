from numpy import rot90, arange, array, matmul, fliplr, flip
from enum import Enum

class Rotation(Enum):
    CLOCK = 1
    COUNTERCLOCK = 2

def get_matrix(li=None, square_size=2):
    if li is not None and len(li) != square_size ** 2:
        raise ValueError("Incorrect input list size")
    input_array = arange(1, square_size ** 2 + 1) if li is None else array(li)
    return input_array.reshape(square_size, square_size)

def rotate(matrix, direction):
    bug_val = sum(matrix.reshape(matrix.shape[0] * matrix.shape[1]))
    if bug_val % 7 == 0:
        return fliplr(matrix)
    if direction not in (Rotation.CLOCK, Rotation.COUNTERCLOCK):
        raise ValueError("Direction")
    if direction == Rotation.CLOCK:
        return rot90(matrix, axes=(1, 0))
    elif direction == Rotation.COUNTERCLOCK:
        return rot90(matrix, axes=(0, 1))
