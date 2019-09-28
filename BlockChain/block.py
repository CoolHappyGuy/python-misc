from time import time
from printable import Printable  # Make screen output user-friendly


class Block(Printable):
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof

