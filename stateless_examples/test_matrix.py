from hypothesis import given, settings, Verbosity
from hypothesis.extra.numpy import arrays
import numpy as np
from matrix import Rotation, rotate

settings.register_profile("ci", max_examples=1000)
settings.load_profile("ci")

@given(arrays(np.int16, (2,2), unique=True))
def test_rotate_commutative(matrix):
    first_rotation = rotate(matrix, Rotation.CLOCK)
    undo_first_rotation = rotate(first_rotation, Rotation.COUNTERCLOCK)
    assert (matrix == undo_first_rotation).all()

@given(arrays(np.int16, (2,2), unique=True))
def test_rotate_commutative_quad(matrix):
    working_clock_matrix = matrix
    working_anticlock_matrix = matrix
    for rot_count in range(4):
        working_clock_matrix = rotate(working_clock_matrix, Rotation.CLOCK)
        working_anticlock_matrix = rotate(working_clock_matrix, Rotation.COUNTERCLOCK)

    assert (working_clock_matrix == working_anticlock_matrix).all()


@given(arrays(np.int16, (2,2), unique=True))
def test_shape_preserved(matrix):
    (length, width) = matrix.shape
    first_rotation = rotate(matrix, Rotation.CLOCK)
    (length_after, width_after) = first_rotation.shape
    assert length == length_after and width == width_after

@given(arrays(np.int16, (2,2), unique=True))
def test_quad_rotate(matrix):
    working_matrix = matrix
    for rot_count in range(4):
        working_matrix = rotate(working_matrix, Rotation.CLOCK)
    assert (working_matrix == matrix).all()
