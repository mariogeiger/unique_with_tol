import numpy as np
from .unique_with_tol import _unique_with_tol


def unique_with_tol(a: np.array, tol: float, *, axis: int = 0):
    assert a.ndim >= 1
    a = np.moveaxis(a, axis, 0)
    a = a.reshape(a.shape[0], -1)

    return _unique_with_tol(a, tol)
