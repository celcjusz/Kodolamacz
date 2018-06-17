import math

def euclidean_distance(A, B):
    """
    >>> euclidean_distance((0,0), (1,0))
    1.0

    >>> euclidean_distance((0,0), (1,1))
    1.4142135623730951

    >>> euclidean_distance((0,1), (1,1))
    1.0

    >>> euclidean_distance((0,10), (1,1))
    9.055385138137417
    """
    x_diff = A[0] - B[0]
    y_diff = A[1] - B[1]

    x_diff_pow_2 = math.pow(x_diff, 2)
    y_diff_pow_2 = math.pow(y_diff, 2)

    sum_pow = x_diff_pow_2 + y_diff_pow_2

    return math.pow(sum_pow,  0.5)



