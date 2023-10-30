import math

def is_prime(n):
    """
    Test if a given integer is prime.

    Parameters
    ----------
    n : an abitrary interger inputed by the user to be tested if it is a prime or not

    Returns
    -------
    boolean
      True or False based on the inputed integer's primality.

    Examples
    --------
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(7)
    True
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True