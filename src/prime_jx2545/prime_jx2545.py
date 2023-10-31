import math

def is_prime(n):
    """
    Test if a given integer is prime.

    Parameters
    ----------
    n : an abitrary interger inputed by the user to be tested if it is a prime or not

    Returns
    -------
    bool
      True or False based on the inputed integer's primality.

    Examples
    --------
    >>> from prime_jx2545 import prime_jx2545
    >>> n = 2
    >>> prime_jx2545.is_prime(2)
    True
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True