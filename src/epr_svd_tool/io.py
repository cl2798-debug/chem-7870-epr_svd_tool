import numpy as np
from .eprload_BrukerBES3T import eprload_BrukerBES3T
from .eprload_BrukerESP import eprload_BrukerESP


def eprload(filename, scaling=None):
    ext = filename[-4:].lower()
    if ext in [".dsc", ".dta"]:
        return eprload_BrukerBES3T(filename, scaling)
    elif ext in [".spc", ".par"]:
        return eprload_BrukerESP(filename, scaling)
    else:
        raise ValueError(
            f"Unsupported file extension for {filename}. "
            "Expected .DSC, .DTA, .spc, or .par."
        )


def _get_1d_axis(abscissa, data_shape):
    abscissa = np.asarray(abscissa)

    if abscissa.ndim == 1:
        return abscissa.ravel()

    if abscissa.ndim == 2:
        if 1 in abscissa.shape:
            return abscissa.ravel()

        if abscissa.shape[0] == data_shape[0]:
            return abscissa[:, 0].ravel()
        if abscissa.shape[1] == data_shape[0]:
            return abscissa[0, :].ravel()

        if len(data_shape) > 1:
            if abscissa.shape[0] == data_shape[1]:
                return abscissa[:, 0].ravel()
            if abscissa.shape[1] == data_shape[1]:
                return abscissa[0, :].ravel()

    raise ValueError(f"Could not convert abscissa shape {abscissa.shape} to 1D.")


def _orient_kinetic_matrix(data, field_axis):
    data = np.asarray(data)

    if data.ndim == 1:
        return data.reshape(-1, 1)

    if data.ndim != 2:
        raise ValueError(f"Unsupported data shape: {data.shape}")

    if data.shape[0] == len(field_axis):
        return data
    if data.shape[1] == len(field_axis):
        return data.T

    raise ValueError(
        f"Cannot match field axis length {len(field_axis)} with data shape {data.shape}"
    )


def load_bruker_kinetic(filename, scaling=None):
    data, abscissa, par = eprload(filename, scaling=scaling)
    field = _get_1d_axis(abscissa, np.shape(data))
    matrix = _orient_kinetic_matrix(data, field)
    matrix = np.real(matrix)
    return field, matrix, par