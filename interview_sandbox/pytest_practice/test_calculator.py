import pytest
from calculator import divide


# def test_divide_success():
#     assert divide(10, 2) == 5


# def test_divide_error():
#     with pytest.raises(ZeroDivisionError):
#         divide(10, 0)


@pytest.mark.parametrize("number_1, number_2, expected", [
    (10, 2, 5),
    (12, 3, 4),
    (20, 0, ZeroDivisionError)
])
def test_divide_params(number_1, number_2, expected):
    if expected == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            divide(number_1, number_2)
    else:
        assert divide(number_1, number_2) == expected