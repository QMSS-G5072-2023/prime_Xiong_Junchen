from prime_jx2545 import prime_jx2545

def test_is_prime():

    # Test for known prime numbers
    assert prime_jx2545.is_prime(2) == True
    assert prime_jx2545.is_prime(7) == True
    assert prime_jx2545.is_prime(11) == True

    # Assert tests for known composite numbers
    assert prime_jx2545.is_prime(8) == False
    assert prime_jx2545.is_prime(9) == False
