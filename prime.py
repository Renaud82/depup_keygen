import math, random

def isPrime(num):
    # Return num if num is a prime number and False if not
    if (num < 2):
        return False # 0, 1, and negative numbers are not prime.

    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            # It is not a prime number
            return False
    else:
        return(num)

def generateLargePrime(keysize=16):
    # Return a random prime number that is keysize bits in size:
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))

        if isPrime(num):
            return num