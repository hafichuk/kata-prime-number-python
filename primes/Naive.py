def naive(n):
    import math

    """A prime number is a number, larger than 1, that can only be divided evenly by itself and 1"""
    if (n < 2):
        return []

    factorials = []
    divisor = 2

    while n > 1:
        if (n%divisor == 0):
            factorials.append(divisor)
            n = n/divisor
        else:
            divisor = divisor + 1
            if divisor > math.sqrt(n):
                divisor = n

    return factorials