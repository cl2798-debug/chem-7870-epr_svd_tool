import numpy as np
from epr_svd_tool.preprocess import normalize_columns


def test_normalize_columns():
    matrix = np.array([[1.0, 2.0], [2.0, 4.0]])
    out = normalize_columns(matrix)
    assert np.isclose(np.max(np.abs(out[:, 0])), 1.0)
    assert np.isclose(np.max(np.abs(out[:, 1])), 1.0)