from .preprocess import baseline_correct_columns, normalize_columns
from .svd import svd_denoise_matrix


def prepare_kinetic_matrix(field, matrix, poly_order=1, rank=3):
    """
    Full preprocessing + SVD workflow.
    """
    matrix_bc = baseline_correct_columns(field, matrix, poly_order=poly_order)
    matrix_norm = normalize_columns(matrix_bc)
    matrix_svd, singular_values = svd_denoise_matrix(matrix_norm, rank=rank)
    difference = matrix_norm - matrix_svd
    return matrix_norm, matrix_svd, difference, singular_values