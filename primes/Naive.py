def naive(n):
    """A prime number is a number, larger than 1, that can only be divided evenly by itself and 1"""
    if (n < 2):
        return []

    primes = [2]

    if (n in primes):
        return [n]

    return []