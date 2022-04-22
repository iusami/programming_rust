from python.main import gcd
import pytest


@pytest.mark.parametrize(
    "x, y, answer", [
        (10, 5, 5),
        (36, 4, 4)
    ]
)
def test_gcd(x, y, answer):
    assert gcd(x, y) == answer, f"gcd(10,5) should be {answer}"

@pytest.mark.parametrize(
    "x, y, answer", [
        (10, 5, 4),
        (36, 4, 9)
    ]
)
def test_gcd_error(x, y, answer):
    with pytest.raises(AssertionError):
        assert gcd(x, y) == answer, f"gcd(10,5) should be {answer}"
