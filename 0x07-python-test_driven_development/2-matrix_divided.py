#!/usr/bin/python3

"""This module defines the function matrix_divided"""


def matrix_divided(matrix, div):
    """Divide each element of matrix by div.

    Args:
        matrix (list): List of list of (int or float).
        div (int or float): Divides each element of matrix.

    Raises:
        TypeError: If either matirx or div is not the right type.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix obtained from dividing matrix by div.
    """
    err_message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_message)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err_message)
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(err_message)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
