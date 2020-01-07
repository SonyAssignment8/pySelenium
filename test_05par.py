from test_python1 import cal
import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [(5,25),
                          (9,81),
                          (10,100),
                          (4,16),
                          (2,0)
                          ])

def test_cal_square(test_input,expected_output):
    res=cal.cal_square(test_input)
    assert res== expected_output



