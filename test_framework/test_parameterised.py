from test_framework import cal
import pytest
@pytest.mark.parametrize("test_input,expected_output",
                         [(5,25),
                          (9,81),
                        (10,100)
                          ])
def test_cal_square(test_input,expected_output):
    res=cal.calc_square(test_input)
    assert res==expected_output