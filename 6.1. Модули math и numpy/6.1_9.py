import numpy as np


def rotate(matr, gradus):
    for x in range(gradus // 90):
        matr = np.rot90(matr, -1)
    return matr
