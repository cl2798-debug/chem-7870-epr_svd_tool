import numpy as np


def svd_denoise_matrix(matrix, rank=3):
    U, s, Vt = np.linalg.svd(matrix, full_matrices=False)
    rank = max(1, min(rank, len(s)))
    matrix_svd = U[:, :rank] @ np.diag(s[:rank]) @ Vt[:rank, :]
    return matrix_svd, s