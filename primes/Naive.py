def naive(n):
    """A prime number is a number, larger than 1, that can only be divided evenly by itself and 1"""
    if (n < 2):
        return []

    primes = [2, 3, 5]

    if (n in primes):
        return [n]

    factorials = []

    count = len(primes)
    i = 0
    while (i < count):
        if (n % primes[i] == 0):
            factorials.append(primes[i])
            n = n / primes[i]
        else:
            i = i+1

    return factorials