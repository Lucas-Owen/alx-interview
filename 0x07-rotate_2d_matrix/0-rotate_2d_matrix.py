#!/usr/bin/python3
"""This is rotate_2d_matrix function"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d square matrix in-place 90 degrees clockwise"""
    n = len(matrix[0])
    for i in range(n // 2):
        i_tr_inv = n - i - 1
        for j_tr_inv in range(i, i_tr_inv):
            k = n - j_tr_inv - 1
            temp = matrix[i][j_tr_inv]
            matrix[i][j_tr_inv] = matrix[k][i]
            matrix[k][i] = matrix[i_tr_inv][k]
            matrix[i_tr_inv][k] = matrix[j_tr_inv][i_tr_inv]
            matrix[j_tr_inv][i_tr_inv] = temp
