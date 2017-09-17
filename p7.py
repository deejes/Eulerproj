# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

print ('rtes')

def is_prime(x):
    if x < 2:
        return False
    for y in range (2,x):
        if x % y == 0:
            return False
    return True
#    l = [True for x in range(target)]
#    print (l)

primes = []
x = 2
while len(primes) != 6:
    if is_prime(x):
        primes.append(x)
    x +=1


print (primes[-1])
