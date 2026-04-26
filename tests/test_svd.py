import numpy as np
from epr_svd_tool.svd import svd_denoise_matrix


def test_svd_denoise_shape():
    matrix = np.random.randn(100, 20)
    denoised, s = svd_denoise_matrix(matrix, rank=3)
    assert denoised.shape == matrix.shape
    assert len(s) == min(matrix.shape)