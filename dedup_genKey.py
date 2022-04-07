import os, sys
import csv
from tools import dedup, generateKey

# Step 1: check file and directory
inputDirectory = os.getcwd() + "/inputs"
outputDirectory = os.getcwd() + "/outputs"
inputFileDedup = inputDirectory + "/users.csv"
outputFileDedup = outputDirectory + "/dedup_users.csv"

if not os.path.exists(inputFileDedup):
    sys.exit('WARNING: No input file: %s' % inputFileDedup)

if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

# Step 2: file creation with record deduplication
dedup(inputFileDedup, outputFileDedup)

# Step 3: file creation with key generation :
# - Public key
# - Private Key

inputFileGenKey = outputFileDedup
outputFileGenKeyPub = outputDirectory + "/users_PublicKey.csv"
outputFileGenKeyPriv = outputDirectory + "/users_privateKey.csv"

reader = csv.reader(open(inputFileGenKey, 'r'), delimiter=';')
writerPub = csv.writer(open(outputFileGenKeyPub, 'w'), delimiter=';')
writerPriv = csv.writer(open(outputFileGenKeyPriv, 'w'), delimiter=';')

header = True

for row in reader:
    rowPub = row
    rowPriv = row

    if header:
        rowPub.append('Key_Pub')
        rowPriv.append('Key_Priv')
        header = False
    else:
        publicKey, privateKey = generateKey(16)
        rowPub.append(publicKey)
        rowPriv.append(privateKey)

    writerPub.writerow(rowPub)
    writerPriv.writerow(rowPriv)