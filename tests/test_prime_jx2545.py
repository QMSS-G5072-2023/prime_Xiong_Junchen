from prime_jx2545 import prime_jx2545

import pytest


@pytest.mark.parametrize("example, expected", [
    # Known prime numbers
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
    # known composite numbers
        (4, False),
        (6, False),
        (8, False),
        (9, False),
        (12, False),
    # edge cases
        (-100, False),
        (0, False),
        (1, False)])

def test_is_prime_param(example, expected):
    assert prime_jx2545.is_prime(example) == expected
