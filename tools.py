import csv
import math, random
import prime
import cryptomath

def dedup (inputFile,outputFile):

    reader = csv.reader(open(inputFile, 'r'), delimiter=';')
    writer = csv.writer(open(outputFile, 'w'), delimiter=';')

    entries = set()

    for row in reader:
        key = (row[1], row[2])

        if key not in entries:
            writer.writerow(row)
            entries.add(key)

def generateKey(keySize):

    # Creates public/private keys keySize bits in size.
    p= 0
    q= 0

    # Step 1: Create two prime numbers, p and q. Calculate n = p * q:
    #print('Generating p prime...')
    while p == q:
        p = prime.generateLargePrime(keySize)
        q = prime.generateLargePrime(keySize)

    n=p* q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1):
    #print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        # Keep trying random numbers for e until one is valid:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    # Step 3: Calculate d, the mod inverse of e:
    #print('Calculating d that is mod inverse of e...')
    d = cryptomath.findModInverse(e, (p-1) * (q-1))

    publicKey = (n, e)
    privateKey = (n,d)

    return (publicKey, privateKey)