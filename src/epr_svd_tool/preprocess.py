import numpy as np


def baseline_correct_columns(field, matrix, poly_order=1):
    corrected = np.zeros_like(matrix, dtype=float)
    for i in range(matrix.shape[1]):
        y = np.real(matrix[:, i])
        coeffs = np.polyfit(field, y, poly_order)
        baseline = np.polyval(coeffs, field)
        corrected[:, i] = y - baseline
    return corrected


def normalize_columns(matrix):
    out = np.zeros_like(matrix, dtype=float)
    for i in range(matrix.shape[1]):
        y = matrix[:, i]
        scale = np.max(np.abs(y))
        if scale == 0:
            out[:, i] = y
        else:
            out[:, i] = y / scale
    return out
