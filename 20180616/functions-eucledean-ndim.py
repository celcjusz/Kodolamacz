import math


def euclidean_distance_n_dimensions(A, B):
    """
    >>> euclidean_distance_n_dimensions((0,0,0), (0,0,0))
    0.0

    >>> euclidean_distance_n_dimensions((0,0,0), (1,1,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
        ...
    ValueError: Punkty muszą być w przestrzeni tylu-samo wymiarowej
    """
    if len(A) != len(B):
        raise ValueError("Punkty muszą być w przestrzeni tylu-samo wymiarowej")

    coordinates_diff_pow_2_lst = []
    for coordinate in range(0, len(A)):
        coordinate_diff = A[coordinate] - B[coordinate]
        coordinate_diff_pow_2 = math.pow(coordinate_diff, 2)
        coordinates_diff_pow_2_lst.append(coordinate_diff_pow_2)

    sum_args = sum(coordinates_diff_pow_2_lst)

    return math.pow(sum_args, 0.5)