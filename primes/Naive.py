def naive(n):
    """A prime number is a number, larger than 1, that can only be divided evenly by itself and 1"""
    if (n < 2):
        return []

    primes = [2, 3]

    if (n in primes):
        return [n]

    factorials = []

    while (n % primes[0] == 0):
        factorials.append(primes[0])
        n = n / primes[0]

    return factorials