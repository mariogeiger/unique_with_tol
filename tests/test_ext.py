import numpy as np
from unique_with_tol import unique_with_tol


def test_run():
    np.testing.assert_equal(
        unique_with_tol(np.array([1.0, 1.1, 3.0, 3.2]), 1.0),
        np.array([0, 0, 1, 1]),
    )
