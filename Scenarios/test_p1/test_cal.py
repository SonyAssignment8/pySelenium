from test_p1 import cal
import pytest

# test_m1():

@pytest.mark.parametrize("test_input,expected_output",
                         [
                             (5,25),
                             (9,81),
                             (10,100)

                         ])

def test_cal_sqaure(test_input,expected_output):
    res = cal.calc_square(test_input)
    assert res == expected_output

