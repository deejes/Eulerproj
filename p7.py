# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def is_prime(x):
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    for y in range(2, int(x**(1 / 2.0)) + 1):
        if x % y == 0:
            return False
    return True


primes = []
x = 2

while len(primes) != 10001:
    if is_prime(x):
        primes.append(x)
    x += 1

print(primes[-1])
