# Mark Klobukov
# Merkle Tree for ECEC T480 at Drexel U
#4/19/2018
import hashlib

class MerkleTree:
    tree = None
    def __init__(self, transactions):
        self.tree = []
        self.createTree(transactions)

    def createTree(self, transactions):
        #it is assumed that the transactions list consists of
        #transaction hashes, not the actual transactions

        #create a new level of tree
        self.tree.append(transactions)
        #recursion base case:
        if len(transactions) == 1:
            return transactions[0]

        pairedTransactions = []
        #concatenate pairs, hash them, and add them to a new transaction list
        for i in range(0, len(transactions)-1, 2):
            pairedTransactions.append(concatenateAndHash(transactions[i], transactions[i+1]))

        #if the number of transaction is odd, there is one untouched element remaining
        #hash it by itself
        if len(transactions) % 2 == 1:
            pairedTransactions.append(concatenateAndHash(transactions[-1], ''))

        #pass the new transaction list to the next level
        return self.createTree(pairedTransactions)

    def getRoot(self):
        if self.tree != None:
            return self.tree[-1][0]
        return None

#concatenate and hash two elements
def concatenateAndHash(first, second):
    concat = first + second
    return hashlib.sha256(concat).hexdigest()
