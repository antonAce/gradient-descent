import pytest
import numpy as np

from core.grad import *


@pytest.fixture(scope="function", params=[
    (np.array([2.0]), 1e-6, 32.0, 5),
    (np.array([2.0]), 0.01, 32.0, 3),
    (np.array([0.0]), 1e-6, 12.0, 5),
    (np.array([0.0]), 1e-7, 12.0, 6),
    (np.array([-2.0]), 1e-6, 16.0, 5)])
def non_smoothed_single_variable_params(request):
    return request.param


def test_non_smoothed_should_calculate_grad_vector_single_variable(non_smoothed_single_variable_params):
    F = lambda x: x ** 3 + 2 * x ** 2 + 12 * x + 100
    (x0, h, g0, dec) = non_smoothed_single_variable_params # input variable, grid step, expected gradient value, decimal accuracy

    np.testing.assert_almost_equal(grad_left(F, x0, h=h), g0, decimal=dec)
    np.testing.assert_almost_equal(grad_center(F, x0, h=h), g0, decimal=dec)
    np.testing.assert_almost_equal(grad_right(F, x0, h=h), g0, decimal=dec)
