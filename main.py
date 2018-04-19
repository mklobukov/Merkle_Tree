# Mark Klobukov
# Merkle Tree for ECEC T480 at Drexel U
#4/19/2018

from merkle import *
import hashlib, binascii
import sys

expectedEven = "3893b71b473bd5abd8f1b3a5d97eb6d1ccc220eebd702ad1154417cc1cdae20e"
expectedOdd = "5c792810140ac5924925cfbbb3dc0f894b17fdb3f89b39921128711b457de9fc"

def loadTransactionsFromFile(file):
    ts = [] #transactions
    with open(file, 'r') as f:
        for line in f:
            l = line.strip()
            hashedInput = hashlib.sha256(l).hexdigest()
            ts.append(hashedInput)
    return ts

def main():

    #get transactions from the files provided with this assignment
    even = loadTransactionsFromFile("even.txt")
    odd = loadTransactionsFromFile("odd.txt")

    #construct tree for the odd case and for the even case
    oddTree = MerkleTree(odd)
    evenTree = MerkleTree(even)

    #extract roots of the two trees and compare them to the provided ones
    rootEven = evenTree.getRoot()
    rootOdd = oddTree.getRoot()

    print
    print "Expected even root hash: ", expectedEven
    print "Computed even root hash: ", rootEven

    if expectedEven == rootEven:
        print "Even hashes match. Computations correct."
    else:
        print "Even hashes do not match. Computations incorrect."

    print
    print "Expected odd root hash: ", expectedOdd
    print "Computed odd root hash: ", rootOdd
    if expectedOdd == rootOdd:
        print "Odd hashes match. Computations correct."
    else:
        print "Odd hashes do not match. Computations incorrect."
    print
    
if __name__ == "__main__":
    main()
